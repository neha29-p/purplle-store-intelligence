import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import pandas as pd
from pipeline.camera_analyzer import CameraAnalyzer

# -----------------------------
# CCTV ANALYTICS
# -----------------------------

analyzer = CameraAnalyzer()

video_dir = Path("data/videos/CCTV Footage")

camera_results = {}

for video in sorted(video_dir.glob("*.mp4")):
    summary = analyzer.summarize(str(video))
    camera_results[video.stem] = summary

# Find busiest camera
busiest_camera = max(
    camera_results,
    key=lambda x: camera_results[x]["average_occupancy"]
)

# -----------------------------
# POS ANALYTICS
# -----------------------------

df = pd.read_csv(
    "data/pos/Brigade_Bangalore_10_April_26 (1)bc6219c.csv"
)

total_gmv = df["GMV"].sum()
total_nmv = df["NMV"].sum()

df["hour"] = pd.to_datetime(
    df["order_time"],
    format="%H:%M:%S"
).dt.hour

hourly_sales = df.groupby("hour")["NMV"].sum()

peak_sales_hour = hourly_sales.idxmax()
peak_sales_value = hourly_sales.max()

top_brands = df["brand_name"].value_counts().head(3)
top_departments = df["dep_name"].value_counts().head(3)

# -----------------------------
# REPORT
# -----------------------------

print("\n" + "=" * 60)
print("PURPLLE STORE INTELLIGENCE REPORT")
print("=" * 60)

print("\nTRAFFIC ANALYTICS")
print("-" * 30)

for camera, stats in camera_results.items():
    print(
        f"{camera}: "
        f"Avg={stats['average_occupancy']} "
        f"Max={stats['max_occupancy']}"
    )

print(f"\nBusiest Camera: {busiest_camera}")

print("\nSALES ANALYTICS")
print("-" * 30)

print(f"Total GMV: ₹{total_gmv:,.2f}")
print(f"Total NMV: ₹{total_nmv:,.2f}")

print(
    f"Peak Sales Hour: "
    f"{peak_sales_hour}:00 "
    f"(₹{peak_sales_value:,.2f})"
)

print("\nTOP BRANDS")
print("-" * 30)

for brand, count in top_brands.items():
    print(f"{brand}: {count}")

print("\nTOP DEPARTMENTS")
print("-" * 30)

for dept, count in top_departments.items():
    print(f"{dept}: {count}")

print("\nINSIGHTS")
print("-" * 30)

print(
    f"Highest traffic area appears to be {busiest_camera}."
)

print(
    "Makeup products are the strongest department."
)

print(
    f"Sales peak around {peak_sales_hour}:00."
)

print("\n" + "=" * 60)
