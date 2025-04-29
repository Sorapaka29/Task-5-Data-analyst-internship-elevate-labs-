import pandas as pd

# Load your dataset (assuming the file is named 'titanic.csv')
df = pd.read_csv('titanic.csv')

# 1. Statistical Exploration

# .describe() gives summary statistics for numeric columns
print("Summary Statistics for Numeric Columns:")
print(df.describe())

# .info() gives a concise summary of the DataFrame, including data types and missing values
print("\nDataframe Info:")
print(df.info())

# 2. Value Counts (for categorical columns)
# To check how many times each value appears in specific columns like 'Survived', 'Pclass', etc.
print("\nValue Counts for 'Survived' column:")
print(df['Survived'].value_counts())

print("\nValue Counts for 'Pclass' column:")
print(df['Pclass'].value_counts())

print("\nValue Counts for 'Sex' column:")
print(df['Sex'].value_counts())

print("\nValue Counts for 'Embarked' column:")
print(df['Embarked'].value_counts())
