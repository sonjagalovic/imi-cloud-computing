import os
from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import precision_recall_fscore_support
import pickle

app = Flask(__name__)

data_path = os.environ.get('data_path', 'wine-quality-white-and-red.csv')
model_path = os.environ.get('model_path', 'wine_model.pkl')

scaler = StandardScaler()
model = MLPClassifier(hidden_layer_sizes=(50, 100, 150, 200), max_iter=300, activation='relu', solver='adam')

@app.route("/train", methods=["POST"])
def train():
    output_column = request.json.get('output_column')
    test_size = request.json.get('test_size', 0.25)

    df = pd.read_csv(data_path)

    x = df.drop(output_column, axis=1)
    y = df[output_column]

    trainX, testX, trainY, testY = train_test_split(x, y, test_size=test_size)

    trainX_scaled = scaler.fit_transform(trainX)
    testX_scaled = scaler.transform(testX)

    model.fit(trainX_scaled, trainY)

    with open(model_path, "wb") as f:
        pickle.dump((model, scaler), f)

    y_pred = model.predict(testX_scaled)

    precision, recall, f1_score, _ = precision_recall_fscore_support(testY, y_pred)

    metrics = {}
    for i, c in enumerate(y.unique()):
        metrics[c] = {
            "precision": str(precision[i]),
            "recall": str(recall[i]),
            "f1 score": str(f1_score[i])
        }
    return jsonify(metrics)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json.get('data')
    data_transformed = scaler.transform(data)
    predictions = model.predict(data_transformed)

    return jsonify({"predictions": predictions.tolist()})

if __name__ == "__main__":
    app.run(host='0.0.0.0')