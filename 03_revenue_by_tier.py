import pandas as pd

df = pd.read_csv("E_commerce_with_tiers.csv")

# Calculating the total revenue contributed by each tier, rounding to two decimal places. 
revenue_by_tier = df.groupby("Engagement Tier")["Transaction Amount"].sum().round(2)

print("Revenue by Tier:")
print(revenue_by_tier)
