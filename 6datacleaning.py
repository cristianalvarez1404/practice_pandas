import pandas as pd
import os

os.system("cls")

"""
fixing/removing , incomplete, incorrect or irrelevant data

~75% of work done with pandas is data cleaning

"""

df = pd.read_csv("sample_data.csv")

#Drop irrelevant columns
# df = df.drop(columns=["Salary", "ID"])

#Handle missing data
# df = df.dropna(subset=["Salary"])
# df = df.fillna({"Salary":0})

#Fix inconsistent values
# df["City"] = df["City"].replace({"San Francisco":"SF","New York":"NY"})

#Standarize text
df["Name"] = df["Name"].str.lower()

#Fix data types
# df["boolean"] = df["boolean"].astype(bool)

#Remove duplicate values
df = df.drop_duplicates()


print(df.to_string())