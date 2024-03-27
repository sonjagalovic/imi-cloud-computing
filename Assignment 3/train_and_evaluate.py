import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

cleaned_dataset_path = sys.argv[1]
target_column = sys.argv[2]
training_percentage = float(sys.argv[3])

df = pd.read_csv(cleaned_dataset_path)

X = df.drop(columns=[target_column])
y = df[target_column]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1-training_percentage, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

rmse = mean_squared_error(y_test, y_pred, squared=False)

print("Calculated RMSE: {:.4f}".format(rmse))