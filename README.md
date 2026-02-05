#  Supermarket Analysis

This project provides insights into supermarket transactions and customer behavior using Python, Pandas, and Streamlit.  
It includes reproducible ETL pipelines, inline visualizations, and a live interactive dashboard.

---

##  Features
- Data cleaning and transformation with **Pandas**
- Interactive dashboard built with **Streamlit**
- Inline visualizations embedded directly in the README
- Deployment-ready for recruiters and collaborators

---

##  Visualizations

<div align="center">

**Premium Customers by Store**  
<img src="images/premium_customers.png" width="300">

**Total Sales by Store**  
<img src="images/total_sales.png" width="300">

**Customer Type Distribution**  
<img src="images/customer_distribution.png" width="300">

</div>

 [View the Live Dashboard](https://nse-stock-pipeline.netlify.app/)

---

##  Dataset
- `supermarket_data.csv` — Raw transactional data
- `sales_by_store.csv` — Aggregated sales per store
- `premium_customers_by_store.csv` — Premium customer counts per store
- `customer_type_distribution.csv` — Distribution of customer types

---

## Tech Stack
- **Python** (Pandas, Seaborn, Matplotlib)
- **Streamlit** for interactive dashboards
- **GitHub** for version control and collaboration

---

##  Author
**Maina Murage** — Big Data Engineer | Cloud‑Native Architect | ETL/Streaming Specialist

---

##  How to Run Locally
Clone the repo and install requirements:

```bash
git clone https://github.com/mainamuragev/supermarket_analysis.git
cd supermarket_analysis
pip install -r requirements.txt
streamlit run dashboard.py

