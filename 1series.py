import pandas as pd
import os

os.system("cls")

"""
Series => A pandas 1-Dimensional labeld array that can hold any data type = Single column in a spreedsheet

"""
# data = [100.1, 102.2, 104.3]
# data = ["A", "B", "C"]
# data = [True,False,True]
# data = [100, 102, 104, 200, 202]

# series = pd.Series(data, index=["apartment #1","apartment #2","apartment #3"])
# series = pd.Series(data, index=["a","b","c","d","e"])

# series.loc["c"] = 200
# print(series.loc["a"])
# print(series.loc["b"])
# print(series.loc["c"])

# print(series.iloc[3])
# print(series[series >= 200])

"""
Dictionaries
"""


calories = {
  "Day 1" : 1750,
  "Day 2" : 2100,
  "Day 3" : 1700
}

series = pd.Series(calories)

# series.loc["Day 3"] += 500

# print(series)
# print(series.loc["Day 3"])
# print(series[series >= 2000])
print(series[series < 2000])