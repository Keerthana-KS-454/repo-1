import pandas as pd

# 1. Load the dataset
df = pd.read_csv("sales_data.csv")

print("Original dataset:")
print(df.head())

# 2. Check dataset information
print("\nDataset information:")
print(df.info())

# 3. Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 4. Remove duplicate rows
print("\nDuplicates before removing:")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("Duplicates after removing:")
print(df.duplicated().sum())

# 5. Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nClean column names:")
print(df.columns)

# 6. Remove extra spaces from text columns
for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip()

# 7. Convert date columns
# Change 'date' to the actual column name if needed
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

# 8. Check data types
print("\nData types:")
print(df.dtypes)

# 9. Handle missing values
# Numeric columns -> fill with median
numeric_columns = df.select_dtypes(include="number").columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# Text columns -> fill with "Unknown"
text_columns = df.select_dtypes(include="object").columns

for column in text_columns:
    df[column] = df[column].fillna("Unknown")

# 10. Final check
print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nFinal dataset:")
print(df.head())

# 11. Save cleaned dataset
df.to_csv("cleaned_sales_data.csv", index=False)

print("\nData cleaning completed successfully!")
print("Cleaned file saved as cleaned_sales_data.csv")
