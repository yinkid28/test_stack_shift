import pandas as pd

# Read from the original file
df = pd.read_csv("E_commerce.csv")

# Ensure Transaction Date is a date type
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])

# Sort by customer and date
df = df.sort_values(by=["Customer ID", "Transaction Date"])

# Using a cumulative count to track previous orders.
# Count prior transactions
df["Prior Purchases"] = df.groupby("Customer ID").cumcount()

# Assign engagement tier
def get_tier(x):
    if x == 0:
        return "New"
    elif 1 <= x <= 4:
        return "Active"
    else:
        return "Power User"

df["Engagement Tier"] = df["Prior Purchases"].apply(get_tier)

# Save processed data
df.to_csv("E_commerce_with_tiers.csv", index=False)
