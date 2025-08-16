import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the CSV file
df = pd.read_csv("orders.csv")

# 1. Make a copy of the file
df_copy = df.copy()
df_copy.to_csv("orders_copy.csv", index=False)

# 2. Calculate total order value for "John Doe" with orders > 100
john_doe_total = df[(df["Customer Name"] == "John Doe") & (df["Order Amount"] > 100)]["Order Amount"].sum()
john_doe_total = round(john_doe_total)

print(f"Total order value for John Doe (orders > $100): {john_doe_total}")

# 3. Country with highest total revenue for orders > 100
country_totals = df[df["Order Amount"] > 100].groupby("Country")["Order Amount"].sum()
country_totals = country_totals.round()
top_country = country_totals.idxmax()
top_country_value = country_totals.max()

print(f"Country with highest total revenue (orders > $100): {top_country} (${top_country_value})")

# 4. Average order amount across all orders > 100
avg_order_over_100 = df[df["Order Amount"] > 100]["Order Amount"].mean()
avg_order_over_100 = round(avg_order_over_100)

print(f"Average order amount (orders > $100): {avg_order_over_100}")

# 5. Bar chart: total revenue by country (orders > 50)
revenue_by_country = df[df["Order Amount"] > 50].groupby("Country")["Order Amount"].sum().round()

plt.bar(revenue_by_country.index, revenue_by_country.values)
plt.title("Total Revenue by Country (Orders > $50)")
plt.xlabel("Country")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
