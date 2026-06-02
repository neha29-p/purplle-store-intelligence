import pandas as pd

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/pos/Brigade_Bangalore_10_April_26 (1)bc6219c.csv"
)

df["hour"] = pd.to_datetime(
    df["order_time"],
    format="%H:%M:%S"
).dt.hour

sales = (
    df.groupby("hour")["NMV"]
      .sum()
      .sort_index()
)

plt.figure(figsize=(8, 4))
plt.plot(sales.index, sales.values, marker="o")

plt.title("Hourly Sales Revenue")
plt.xlabel("Hour")
plt.ylabel("Revenue (₹)")
plt.grid(True)

plt.tight_layout()

plt.savefig("outputs/hourly_sales.png")

print("Saved: outputs/hourly_sales.png")