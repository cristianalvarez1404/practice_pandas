import pandas as pd
import os

os.system("cls")


# df = pd.read_json('sample_data.json')

# print(df.to_string())

df = pd.read_csv('sample_data.csv', index_col="Name")
# print(df.to_string())

#SELECTION BY COLUMN
# print(df["Name"].to_string())
# print(df["City"])
# print(df[["Name","City","Salary"]].to_string())

# SELECTION BY ROW/ROWS
# print(df.loc["Edward",["Age","Salary"]] )
# print(df.iloc[0:11:2, 0:3])

person = input("Enter a person name: ")

try:
  print(df.loc[person])
except KeyError as e:
  print(f"{person} not found")
