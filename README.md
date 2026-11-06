# Superstore Sales Analytics 📊

An end-to-end data analysis project focusing on automated data cleaning and SQL-driven KPI analysis on the Superstore Retail dataset.

---

## 🎯 Project Highlights
- **Automated Data Cleaning Pipeline (`data_cleaning.py`)**:
  - Standardizes column naming conventions.
  - Automatically parses dates (`Order Date`, `Ship Date`).
  - Cleans monetary fields (strips currency symbols and commas, coerces types).
  - Handles missing values and drops corrupt records.
- **In-Memory SQL KPI Engine (`kpi_analysis.py`)**:
  - Leverages SQLite to load cleaned sales records into memory.
  - Executes SQL aggregation queries to answer key business questions:
    - **Revenue & Profit by Region**: Identifies high-performing and underperforming territories.
    - **Top 10 Best-Selling Products**: Highlights revenue drivers by category.
    - **Monthly Sales Trends**: Tracks historical monthly revenue trends.

---

## 🗂️ Project Structure

```text
Superstore_Sales_Analytics/
├── Superstore.csv            # Raw dataset
├── cleaned_superstore.csv    # Cleaned & processed dataset
├── data_cleaning.py          # Preprocessing & cleaning script
├── kpi_analysis.py           # SQL queries & KPI reporting script
├── .gitignore                # Git ignore configuration
└── README.md                 # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python installed with the necessary packages:
```bash
pip install pandas numpy
```
*(SQLite3 is bundled in Python standard library)*

### 2. Run Data Cleaning
To process the raw `Superstore.csv` file into `cleaned_superstore.csv`:
```bash
python data_cleaning.py
```

### 3. Run KPI Analysis
To run SQL queries against the cleaned dataset and view key performance metrics:
```bash
python kpi_analysis.py
```

