import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("E_commerce_with_tiers.csv")

# --- Chart 1: Monthly revenue trends by Region ---
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])
df["Month-Year"] = df["Transaction Date"].dt.to_period("M").astype(str)

monthly_region = df.groupby(["Month-Year", "Region"])["Transaction Amount"].sum().unstack().fillna(0)

monthly_region.plot(kind="line", figsize=(12,6))
plt.title("Monthly Revenue by Region (2022-2024)")
plt.xlabel("Month-Year")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Chart 2: Revenue by Category in 2024 ---
df_2024 = df[df["Transaction Date"].dt.year == 2024]
category_2024 = df_2024.groupby("Category")["Transaction Amount"].sum()

category_2024.plot(kind="bar", figsize=(8,6))
plt.title("Revenue by Category (2024)")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


print(df_2024.head())   # check if we have 2024 rows
print(category_2024)    # check totals per category
