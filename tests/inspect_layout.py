import pandas as pd

df = pd.read_excel(
    "data/layouts/Brigade Road - Store layoutc5f5d56.xlsx",
    header=None
)

print(df.head(30))