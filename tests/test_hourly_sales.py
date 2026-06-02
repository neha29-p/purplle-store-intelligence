import pandas as pd

df = pd.read_csv(
    "data/pos/Brigade_Bangalore_10_April_26 (1)bc6219c.csv"
)

df["hour"] = pd.to_datetime(
    df["order_time"]
).dt.hour

sales = (
    df.groupby("hour")["NMV"]
      .sum()
      .sort_index()
)

print(sales)