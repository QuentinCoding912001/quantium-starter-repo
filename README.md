# Quantium Software Engineering Virtual Experience

This repository contains my work for the Quantium Software Engineering Job Simulation on Forage. It demonstrates an end-to-end data workflow: from raw data processing to visualization and business insight generation using Python.

---

## Project Objective

The goal of this project was to analyze sales data for Soul Foods and answer the key business question:

> **Were sales higher before or after the Pink Morsel price increase on January 15, 2021?**

---

## Project Structure

data/ # Raw input datasets
sales_transformation.py # Data processing and transformation script
formatted_sales_data.csv # Cleaned and combined dataset
sales_report_visualization.py # Dash application for visualization
README.md # Project documentation
.gitignore # Ignored files


---

## Tools & Technologies Used

- Python 3  
- Pandas (data processing and transformation)  
- Plotly (data visualization)  
- Dash (interactive dashboard)  
- Git & GitHub (version control)  
- PowerShell (command line execution)

---

## Task Breakdown & Process

### Task 1 — Repository Setup

- Cloned the starter repository
- Set up Git version control
- Created and published a GitHub repository
- Organized project structure for clarity and maintainability

---

### Task 2 — Data Transformation

Developed a Python script (`sales_transformation.py`) to process raw datasets.

#### Steps performed:
- Loaded multiple CSV/Excel files from the data folder
- Standardized column names for consistency
- Filtered dataset to include only **Pink Morsels**
- Cleaned the `price` field (removed `$` and commas)
- Converted `quantity` and `price` to numeric values
- Created a new field:



---

## Tools & Technologies Used

- Python 3  
- Pandas (data processing and transformation)  
- Plotly (data visualization)  
- Dash (interactive dashboard)  
- Git & GitHub (version control)  
- PowerShell (command line execution)

---

## Task Breakdown & Process

### Task 1 — Repository Setup

- Cloned the starter repository
- Set up Git version control
- Created and published a GitHub repository
- Organized project structure for clarity and maintainability

---

### Task 2 — Data Transformation

Developed a Python script (`sales_transformation.py`) to process raw datasets.

#### Steps performed:
- Loaded multiple CSV/Excel files from the data folder
- Standardized column names for consistency
- Filtered dataset to include only **Pink Morsels**
- Cleaned the `price` field (removed `$` and commas)
- Converted `quantity` and `price` to numeric values
- Created a new field:



- Selected only relevant fields:
  - Sales
  - Date
  - Region

- Combined all datasets into a single structured output file:




---

### Task 3 — Data Visualization

Built an interactive dashboard using Dash (`sales_report_visualization.py`).

#### Features:
- Clear header with project title and author
- Line chart showing **total sales over time**
- Proper axis labels (Date vs Sales)
- Vertical marker indicating **January 15, 2021 (price increase)**
- Summary metrics:
  - Average sales before the price increase
  - Average sales after the price increase
  - Percentage change
- Embedded business insight directly in the dashboard

---

## Key Business Insight

Sales were significantly higher after the price increase on January 15, 2021.

- Before the increase: sales remained consistently below ~7,000  
- After the increase: sales shifted to a higher range (~8,500–9,500)  

Although there were short-term fluctuations, the overall level of sales increased. This indicates that the price increase did not negatively impact demand and resulted in higher total revenue.

---

## How to Run the Project

### 1. Install dependencies

```bash
py -m pip install pandas dash plotly openpyxl

py sales_transformation.py

formatted_sales_data.csv

py sales_report_visualization.py

Then open your browser and go to:
http://127.0.0.1:8050/




