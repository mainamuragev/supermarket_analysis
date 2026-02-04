```markdown
# 🛒 Supermarket Analysis

## 📌 Project Overview
This project demonstrates a **data engineering workflow** for analyzing supermarket transactions. It covers:
- ETL pipeline (Python → PostgreSQL)
- Query optimization with functional indexes
- Terminal‑based visualizations (SQL → CSV → gnuplot → PNG)
- Interactive dashboards (Streamlit deployment)

---

## ⚙️ Tech Stack
- PostgreSQL (Aiven Cloud)
- Python (ETL + automation)
- SQL (schema design, queries, optimization)
- gnuplot + feh (terminal visualizations)
- Streamlit (dashboards)

---

## 📂 Data Model
Main table: `transactions`

| Column           | Type    | Description                  |
|------------------|---------|------------------------------|
| transaction_id   | SERIAL  | Primary key                  |
| store            | TEXT    | Store name                   |
| customer_type    | TEXT    | Member / Non‑member / Premium|
| product_line     | TEXT    | Product category             |
| total_amount     | NUMERIC | Transaction total            |
| transaction_date | DATE    | Date of purchase             |

---

## 🚀 ETL Pipeline
1. **Extract**: Raw CSV data ingested via Python.
2. **Transform**: Cleaned, normalized, enriched.
3. **Load**: Inserted into PostgreSQL `transactions` table.

---

## 🔍 Query Optimization

### Before Indexes
```sql
EXPLAIN ANALYZE SELECT SUM(total_amount)
FROM transactions
WHERE LOWER(store)='bakershire'
  AND LOWER(customer_type)='non-member';
```
Execution Time: **39 ms**

### After Functional Indexes
```sql
CREATE INDEX idx_store_lower ON transactions (LOWER(store));
CREATE INDEX idx_customer_type_lower ON transactions (LOWER(customer_type));
```
Execution Time: **1.3 ms** ✅ **30x faster**

---

## 📊 Visualizations

### Premium Customers by Store
`[Looks like the result wasn't safe to show. Let's switch things up and try something else!]`

### Total Sales by Store
`[Looks like the result wasn't safe to show. Let's switch things up and try something else!]`

### Customer Type Distribution
`[Looks like the result wasn't safe to show. Let's switch things up and try something else!]`

---

## 📈 Dashboards
Interactive dashboards deployed with **Streamlit**:

- **Customer Insights Dashboard**  
  Visualizes premium vs non‑member distribution, store sales, and product line breakdown.  
  👉 Live Demo [(supermarket-analysis.streamlit.app in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fsupermarket-analysis.streamlit.app%2F") *(replace with your actual Streamlit Cloud link)*

---

## 📊 Key Takeaways
- Functional indexes dramatically improve query performance when filtering with `LOWER()`.  
- Queries scale efficiently even as data volume grows.  
- Visualizations highlight **business insights**: premium customer concentration, sales distribution, and customer type mix.  
- Dashboards make insights accessible to non‑technical stakeholders.

---

## 👨‍💻 Author
**Maina Murage**  
Big Data Engineer | Cloud‑Native Architect | ETL/Streaming Specialist  
Focused on reproducible analytics pipelines and performance optimization.
```

---
