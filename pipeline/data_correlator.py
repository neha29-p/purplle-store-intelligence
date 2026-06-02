import pandas as pd
from pathlib import Path

def get_transaction_counts(csv_path):
    # Load the POS data
    df = pd.read_csv(csv_path)
    
    # Convert time column to datetime (Assuming 'order_time' is the header)
    df['order_time'] = pd.to_datetime(df['order_time'])
    
    # Group by hour to match your occupancy sampling
    hourly_sales = df.resample('H', on='order_time').size()
    return hourly_sales

# Usage example:
# csv_file = "data/pos/Brigade_Bangalore_10_April_26.csv"
# sales_data = get_transaction_counts(csv_file)
# print(sales_data)