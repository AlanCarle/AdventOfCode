# 2024 Advent of Code - 1st of Dec

# Code Format

# Import the list (from "Source Numbers.csv")
# sort each column individually
# create new column containing the difference
# sum the difference

import pandas as pd

df_numbers = pd.read_csv('Source Numbers.csv')

for col in df_numbers:
    df_numbers[col] = df_numbers[col].sort_values(ignore_index=True)

df_numbers["Difference"] = abs(df_numbers["Col1"] - df_numbers["Col2"])

print(df_numbers.head())

print(df_numbers['Difference'].sum())
