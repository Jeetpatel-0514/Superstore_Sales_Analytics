import pandas as pd
import sqlite3

def run_kpi_analysis():
    print("Loading cleaned dataset into local SQL database...")
    try:
        df = pd.read_csv("cleaned_superstore.csv")
    except FileNotFoundError:
        print("Error: cleaned_superstore.csv not found. Please run data_cleaning.py first.")
        return

    # Connect to in-memory SQLite database
    conn = sqlite3.connect(':memory:')
    
    # Write the dataframe to a SQL table named 'sales_data'
    df.to_sql('sales_data', conn, index=False, if_exists='replace')

    # Define our SQL Queries
    queries = {
        "1. Revenue and Profit by Region": """
            SELECT 
                region, 
                ROUND(SUM(sales), 2) as total_revenue, 
                ROUND(SUM(profit), 2) as total_profit
            FROM sales_data
            GROUP BY region
            ORDER BY total_revenue DESC;
        """,
        "2. Top 10 Best-Selling Products (by Revenue)": """
            SELECT 
                product_name, 
                category,
                ROUND(SUM(sales), 2) as total_revenue
            FROM sales_data
            GROUP BY product_name, category
            ORDER BY total_revenue DESC
            LIMIT 10;
        """,
        "3. Monthly Sales Trends": """
            SELECT 
                strftime('%Y-%m', order_date) as order_month, 
                ROUND(SUM(sales), 2) as monthly_revenue
            FROM sales_data
            GROUP BY order_month
            ORDER BY order_month ASC;
        """
    }

    print("\n" + "="*50)
    print("SUPERSTORE SALES KPI ANALYSIS (SQL)")
    print("="*50)

    for title, query in queries.items():
        print(f"\n--- {title} ---")
        result_df = pd.read_sql_query(query, conn)
        # Print without index for cleaner formatting
        print(result_df.to_string(index=False))

    conn.close()

if __name__ == "__main__":
    run_kpi_analysis()
