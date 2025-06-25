# Coca-Cola Stock Data Analysis (1962–2025)

**Portfolio Project for Data Analyst Role**

---

## Project Overview

This project offers a comprehensive analysis of historical stock data for **The Coca-Cola Company**, covering the period from **September 6, 1962** to **May 12, 2025**. The goal is to:

- Demonstrate the full data analysis pipeline,
- Perform statistical analysis of long-term stock trends,
- Create clear and informative visualizations.

---

## Data Source

- Dataset: `KO_1919-09-06_2025-05-12.csv`
  - Source: downloaded from **Kaggle**
  - Contains: date, open/close prices, volume, and other market indicators.

---

## Project Structure

```
├── KO_1919-09-06_2025-05-12.csv # formated Coca-Cola stock market data
├── main.py # main script to run
├── plots.py # Script for generating visualizations
├── analysis.py # Script for statistical analysis
├── plots/ # Output charts and plots
└── analysis/ # statistical results
```

---

## Analysis Workflow

The project follows a structured and modular data analysis process:

### 1. Data Acquisition  
- Raw stock data was downloaded from **Kaggle** using their **official API**.

---

### 2. Database Creation  
- A local PostgreSQL database `project_database` was created from the file `KO_1919-09-06_2025-05-12.csv`.  
- The data was imported into a table called `CocaCola_stock_date`.

**CSV adjustments:**
- Extracted column names from **row 1** (since the file lacked a proper header).
- Skipped **row 2**, which contained irrelevant values.
- Loaded actual data starting from **row 3**.

---

### 3. Data Validation & Preprocessing  
A preliminary check ensured data quality:

- Validated column headers  
- Checked for missing (`NULL`) values  
- Detected duplicates in the `date` column  

---

### 4. Data Cleaning & Transformation  
Database values and types were adjusted for analysis:

| Column       | Old Type | New Type | Transformation                     |
|--------------|----------|----------|------------------------------------|
| `open`       | text     | real     | Rounded to 5 decimal places        |
| `high`       | text     | real     | Rounded to 5 decimal places        |
| `low`        | text     | real     | Rounded to 5 decimal places        |
| `close`      | text     | real     | Rounded to 5 decimal places        |
| `adj_close`  | text     | real     | Rounded to 5 decimal places        |
| `volume`     | text     | integer  | Converted to integer               |

---

### 5. Statistical Analysis & Visualization  

Scripts used:
- `main.py`: Master script that runs the full pipeline (`analysis.py` + `plots.py`)  
- `analysis.py`: Computes descriptive statistics and prepares analysis results  
- `plots.py`: Creates visualizations using `Matplotlib`, `Seaborn`, and `Plotly`

**Included analyses and outputs:**

#### Summary Statistics
Key indicators calculated from the dataset:

- Mean opening price: **18.53**  
- Mean closing price: **18.54**  
- Mean adjusted close: **12.92**  
- Std. deviation (adj close): **16.79**  
- Std. deviation (volume): **7,957,798.46**  
- Mean daily return (%): **0.06**  
- Mean trading volume: **9,346,883**  
- Correlation between close and adj_close: **0.97**

> **The full statistical report is available in `report.pdf`**

---

#### Visualizations:
- **Line plot** of stock prices over time
- **50-day and 200-day moving averages**
- **Heatmap** showing correlations between financial indicators
- **30-day rolling standard deviation** of adjusted close (volatility)
- **Monthly average prices**:
  - 10 most recent years (as subplots)
  - Last 63 years (overlayed)
  - 3 grouped charts (21 years per group)
- Consistent visual styling with custom `save_figure()` utility

All charts are saved in the `plots/` directory  
Calculated metrics and exports are saved in `analysis/`  
Final summary delivered in `report.pdf`

---
