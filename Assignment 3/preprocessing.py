import sys
import pandas as pd

file_path = sys.argv[1]

df = pd.read_csv(file_path)

def remove_outliers(df):
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outlier_indices = ((df < lower_bound) | (df > upper_bound)).any(axis=1)
    
    df = df[~outlier_indices]
    
    return df

df = remove_outliers(df)

def fill_missing_values(df):
    df = df.fillna(df.mean())
    return df

df = fill_missing_values(df)

sys.stdout.write(df.to_csv(index=False))