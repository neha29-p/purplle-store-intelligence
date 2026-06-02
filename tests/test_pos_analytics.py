import pandas as pd

df = pd.read_csv(
    "data/pos/Brigade_Bangalore_10_April_26 (1)bc6219c.csv"
)

print("\nPOS Summary")
print("-" * 40)

print("Rows:", len(df))

print("Total GMV:", round(df["GMV"].sum(), 2))
print("Total NMV:", round(df["NMV"].sum(), 2))

print("\nTop 5 Brands")
print(df["brand_name"].value_counts().head())

print("\nTop 5 Departments")
print(df["dep_name"].value_counts().head())