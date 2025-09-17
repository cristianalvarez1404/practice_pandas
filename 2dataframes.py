import pandas as pd
import os

os.system("cls")


"""
Dataframe => A tabular data structure with rows and columns. (2 dimensional)
            Similar to an Excel spreadsheet
"""

data = {
  "Name": ["Spongebob","Patrick","Squidward"],
  "Age" : [30, 35, 50]
}

df = pd.DataFrame(data, index = ["Employee 1", "Employee 2", "Employee 3"])

# print(df.loc["Employee 1"])
# print(df.iloc[0])

#Add a new column

df["Job"] = ["Cook", "N/A", "Cashier"]

# Add a new rows
new_rows = pd.DataFrame([
  {"Name":"Sandy","Age":28,"Job":"Engineer"},
  {"Name":"Eugene","Age":60,"Job":"Manager"},
], index=["Employee 4", "Employee 5"])
df = pd.concat([df,new_rows])

print(df)