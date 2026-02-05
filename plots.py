import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# Premium Customers by Store
premium = pd.read_csv("premium_customers_by_store.csv")
plt.figure(figsize=(8,5))
sns.barplot(data=premium, x="store", y="premium_count", hue="store", dodge=False, legend=False, palette="Blues_d")
plt.title("Premium Customers by Store")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("images/premium_customers.png")
plt.close()

# Total Sales by Store
sales = pd.read_csv("sales_by_store.csv")
plt.figure(figsize=(8,5))
sns.barplot(data=sales, x="store", y="total_sales", hue="store", dodge=False, legend=False, palette="Greens_d")
plt.title("Total Sales by Store")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("images/total_sales.png")
plt.close()

# Customer Type Distribution
cust = pd.read_csv("customer_type_distribution.csv")
plt.figure(figsize=(6,6))
plt.pie(cust["count"], labels=cust["customer_type"], autopct="%1.1f%%", startangle=140)
plt.title("Customer Type Distribution")
plt.tight_layout()
plt.savefig("images/customer_distribution.png")
plt.close()

