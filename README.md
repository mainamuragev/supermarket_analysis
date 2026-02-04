# 🛒 Supermarket Analysis

## 📌 Overview
End‑to‑end supermarket transaction analysis:
- ETL pipeline (Python → PostgreSQL)
- Query optimization with functional indexes
- Visualizations (gnuplot PNGs)
- Interactive dashboard (Streamlit)

---

## ⚙️ Tech Stack
PostgreSQL · Python · SQL · gnuplot · Streamlit

---

## 📂 Data Model
`transactions` table:
- `transaction_id` (PK)
- `store`
- `customer_type`
- `product_line`
- `total_amount`
- `transaction_date`

---

## 🚀 ETL & Optimization
- Raw CSV → cleaned → loaded into PostgreSQL  
- Functional indexes (`LOWER(store)`, `LOWER(customer_type)`) → **30x faster queries**

---

## 📊 Visualizations

### Premium Customers by Store
![Premium Customers](images/premium_customers_by_store.png)

### Total Sales by Store
![Total Sales](images/sales_by_store.png)

### Customer Type Distribution
![Customer Types](images/customer_type_distribution.png)

---

## 📈 Dashboard
Interactive dashboard with **Streamlit**:
👉 [Live Demo](https://supermarket-analysis.streamlit.app)

---

## 👨‍💻 Author
**Maina Murage** — Big Data Engineer | Cloud‑Native Architect | ETL/Streaming Specialist

