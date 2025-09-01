## Supermart Exploratory Data Analysis Project

[![SQL](https://img.shields.io/badge/SQL-Skills-blue)](https://www.sql.org/)  
[![Python](https://img.shields.io/badge/Python-Skills-yellowgreen)](https://www.python.org/)  


## Project Overview

**Project Title:** Supermart Data Analysis  

This project is an end-to-end data analysis solution designed to extract critical business insights from a Supermart sales dataset. Python is used for data processing and analysis, while SQL is leveraged for advanced querying and solving business problems.



## Objectives

<details>
<summary>Click to expand Objectives</summary>

1. Perform data cleaning and preprocessing to ensure accurate analysis.  
2. Conduct feature engineering, including calculating total transaction amounts.  
3. Load the cleaned data into MySQL and PostgreSQL databases.  
4. Write complex SQL queries to answer business questions, such as:
   - Revenue trends across branches and categories  
   - Best-selling product categories  
   - Sales performance by time, city, and payment method  
   - Peak sales periods and customer buying patterns  
   - Profit margin analysis by branch and category  

</details>



## Dataset

- [Kaggle Supermart Dataset](https://www.kaggle.com/datasets/analpatil/supermart-dataset)  
- File path in Kaggle Notebook: `/kaggle/input/Supermart Dataset/supermart.csv`  




## Project Structure
<details>
<summary>Click to expand Objectives</summary>
   
```plaintext
|-- data/                     # Raw data and transformed data
|-- sql_queries/              # SQL scripts for analysis and queries
|-- notebooks/                # Jupyter notebooks for Python analysis
|-- README.md                 # Project documentation
|-- requirements.txt          # List of required Python libraries
|-- main.py                   # Main script for loading, cleaning, and processing data
```
</details>

## Project Setup

<details>
<summary>Click to expand Project Structure</summary>

1. **Environment Setup**
   - Tools: VS Code, Python, SQL (MySQL & PostgreSQL), Anaconda  
   - Organized workspace and project folders for smooth development  

2. **Data Loading**
   - Load CSV into Pandas DataFrame  
   - Explore data using `.info()`, `.head()`, `.describe()`  

3. **Data Cleaning**
   - Remove duplicates and handle missing values  
   - Convert data types (dates as `datetime`, prices as `float`)  
   - Format currency values correctly  

4. **Feature Engineering**
   - Compute `Total_Amount` = `unit_price * quantity`  

5. **Database Loading**
   - Connect to MySQL and PostgreSQL using sqlalchemy  
   - Create tables and insert cleaned data  

6. **SQL Analysis**
   - Revenue by branch, category, and city  
   - Best-selling product categories  
   - Sales patterns by time, payment method, and customer  
   - Profit margin analysis  

7. **Documentation**
   - Maintain clear notes and Markdown/Jupyter Notebook records  

</details>

---

## Findings and Insights

<details>
<summary>Click to expand Findings</summary>

- **Sales Insights**: Key product categories, high-performing branches, and popular payment methods.  
- **Profitability**: Most profitable product categories and branches.  
- **Customer Behaviour**: Buying patterns, peak shopping hours, and preferred payment methods.  
- **Best-Selling Products**: Top-selling products and peak sales periods.  
 

</details>

---

## Conclusion

<details>
<summary>Click to expand Conclusion</summary>

This project demonstrates how to clean, analyze, and derive insights from a retail sales dataset using Python and SQL.  
It provides actionable business insights on revenue trends, sales performance, customer behavior, and product profitability, which can help in decision-making and strategy planning.  

</details>

---

## Author

<details>
<summary>Click to expand Author</summary>

**Anal Patil**  

Portfolio project showcasing SQL and Python skills essential for data analyst roles. Questions, feedback, or collaboration requests are welcome.  

</details>

## Acknowledgments
<details>
<summary>Click to expand Author</summary>
   
- **Data Source**: Kaggle’s Walmart Sales Dataset
- **Inspiration**: Walmart’s business case studies on sales and supply chain optimization.
   
</details>

## Future Enhancements
<details>
<summary>Click to expand Author</summary>
   
Possible extensions to this project:
- Integration with a dashboard tool (e.g., Power BI or Tableau) for interactive visualization.
- Additional data sources to enhance analysis depth.
- Automation of the data pipeline for real-time data ingestion and analysis.
- 
</details>

---



---
