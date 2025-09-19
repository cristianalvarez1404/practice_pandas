import pandas as pd
import os

os.system('cls')

"Reduces a set of values into a single summary value"

df = pd.read_csv("sample_data.csv")

# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count(numeric_only=True))

"Single column"
# print(df["Salary"].mean(numeric_only=True))
# print(df["Salary"].sum(numeric_only=True))
# print(df["Salary"].max(numeric_only=True))

group = df.groupby("City")

# print(group["Salary"].mean(numeric_only=True))
# print(group["Salary"].sum(numeric_only=True))
print(group["Salary"].min(numeric_only=True))