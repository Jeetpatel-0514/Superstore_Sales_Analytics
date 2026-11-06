import pandas as pd
import numpy as np

def clean_data():
    print("Loading Superstore Sales dataset...")
    # The Global Superstore CSV often has 'latin1' encoding
    try:
        df = pd.read_csv("Superstore.csv", encoding="latin1")
    except FileNotFoundError:
        print("Error: Superstore.csv not found. Please ensure it's in the same directory.")
        return

    print("Initial Data Shape:", df.shape)

    # 1. Standardize column names (replace spaces with underscores, make lowercase)
    df.columns = [col.strip().replace(" ", "_").replace("-", "_").lower() for col in df.columns]
    print("\nColumns standardized.")

    # 2. Handle Date columns (Order Date, Ship Date)
    # The format might be DD-MM-YYYY or MM/DD/YYYY, let pandas infer it, but specify dayfirst if needed.
    if 'order_date' in df.columns:
        df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    if 'ship_date' in df.columns:
        df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce')
    print("Dates converted to datetime.")

    # 3. Handle missing values
    # Let's check for missing values in critical columns
    missing_before = df.isnull().sum().sum()
    if 'postal_code' in df.columns:
        # Depending on pandas version, fillna on a column inplace might be deprecated, but it works for now.
        df['postal_code'] = df['postal_code'].fillna('Unknown')
    
    # Drop rows where critical financial columns might be completely null
    df.dropna(subset=['sales', 'profit', 'order_id'], inplace=True)
    missing_after = df.isnull().sum().sum()
    print(f"Handled missing values. Total missing changed from {missing_before} to {missing_after}.")

    # 4. Clean numerical columns (sometimes sales/profit come as strings with $ signs)
    for col in ['sales', 'profit', 'discount', 'shipping_cost']:
        if col in df.columns and df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.replace('$', '').str.replace(',', '')
            df[col] = pd.to_numeric(df[col], errors='coerce')

    print("Numerical columns cleaned.")

    # Save cleaned data
    output_filename = "cleaned_superstore.csv"
    df.to_csv(output_filename, index=False)
    print(f"\nData cleaning complete! Saved to '{output_filename}'.")
    print("Final Data Shape:", df.shape)

if __name__ == "__main__":
    clean_data()
