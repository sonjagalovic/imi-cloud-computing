import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

dataset_file = os.environ.get('DATASET_FILE')
target_column = os.environ.get('TARGET_COLUMN')
k = int(os.environ.get('K'))
current_fold = int(os.environ.get('CURRENT_FOLD'))

df = pd.read_csv(dataset_file)
df = df.fillna(df.mean())

chunk_size = int(len(df) / k)

X = df.drop(columns=[target_column])
y = df[target_column]

X_train = X.iloc[np.r_[0 : current_fold * chunk_size, chunk_size * (current_fold + 1) : len(X)]]
y_train = y[np.r_[0 : current_fold * chunk_size, chunk_size * (current_fold + 1) : len(X)]]
X_test = X[chunk_size * current_fold : chunk_size * (current_fold + 1)]
y_test = y[chunk_size * current_fold : chunk_size * (current_fold + 1)]

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)

print(rmse)