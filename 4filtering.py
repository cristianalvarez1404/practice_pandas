import pandas as pd
import os

os.system('cls')

sample_data = pd.read_csv("sample_data.csv")

df = pd.DataFrame(sample_data)

# age_filter = df[df["Age"] >= 55]
salary_filter  = df[df["Salary"] > 6500]
salary_filter2  = df[df["Salary"] == 6500]
salary_filter3 = df[(df["Salary"] > 6500) & (df["Age"] > 50)]
salary_filter4 = df[(df["Salary"] > 6500) | (df["Age"] > 50)]

print(salary_filter4)