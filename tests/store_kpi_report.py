import pandas as pd

df = pd.read_csv(
    "data/pos/Brigade_Bangalore_10_April_26 (1)bc6219c.csv"
)

df["hour"] = pd.to_datetime(
    df["order_time"],
    format="%H:%M:%S"
).dt.hour

print("\nSTORE KPI REPORT")
print("=" * 50)

print(f"Total Transactions : {len(df)}")
print(f"Total GMV          : ₹{df['GMV'].sum():,.2f}")
print(f"Total NMV          : ₹{df['NMV'].sum():,.2f}")

peak_hour = (
    df.groupby("hour")["NMV"]
      .sum()
      .idxmax()
)

peak_sales = (
    df.groupby("hour")["NMV"]
      .sum()
      .max()
)

print(f"\nPeak Sales Hour    : {peak_hour}:00")
print(f"Peak Hour Revenue  : ₹{peak_sales:,.2f}")

print("\nTop Brand:")
print(df["brand_name"].value_counts().head(1))

print("\nTop Department:")
print(df["dep_name"].value_counts().head(1))