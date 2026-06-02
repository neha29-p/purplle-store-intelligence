import pandas as pd

def get_pos_metrics(csv_path):
    # Load the CSV
    df = pd.read_csv(csv_path)
    
    # Combine date and time into a proper datetime object
    # Using format='%d-%m-%Y' to match your '10-04-2026' format
    df['datetime'] = pd.to_datetime(df['order_date'] + ' ' + df['order_time'], format='%d-%m-%Y %H:%M:%S')
    
    # Filter for the target date
    target_date = pd.Timestamp('2026-04-10')
    daily_sales = df[df['datetime'].dt.date == target_date.date()]
    
    # Calculate metrics
    total_transactions = daily_sales['order_id'].nunique()
    total_nmv = daily_sales['NMV'].sum()
    
    return {
        "transactions": int(total_transactions),
        "total_nmv": float(round(total_nmv, 2)),
        "avg_basket_size": float(round(total_nmv / total_transactions, 2)) if total_transactions > 0 else 0.0
    }

if __name__ == "__main__":
    path = "data/pos/Brigade_Bangalore_10_April_26 (1)bc6219c.csv"
    metrics = get_pos_metrics(path)
    print(f"Business Metrics for April 10th: {metrics}")