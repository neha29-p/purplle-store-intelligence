import pandas as pd

df = pd.read_csv("outputs/cam1_occupancy.csv")

print("\nOccupancy Analytics")
print("-------------------")
print("Average:", round(df["people_count"].mean(), 2))
print("Maximum:", df["people_count"].max())
print("Minimum:", df["people_count"].min())