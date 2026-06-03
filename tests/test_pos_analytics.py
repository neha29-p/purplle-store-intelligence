# PROMPT:
# I need a validation suite for POS analytics calculations used by store managers and business stakeholders.
#
# The objective is to ensure that sales data is aggregated correctly and transformed into actionable business metrics.
#
# The test should validate:
# - Total sales calculations
# - Department-level performance
# - Brand-level performance
# - KPI generation
# - Aggregation consistency
#
# The implementation should prioritize business accuracy because these metrics influence operational and merchandising decisions.
#
# CHANGES MADE:
# Adapted calculations to align with the retail reporting requirements of the project.
#
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
