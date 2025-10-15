# -----------------------------------------
# 📊 Superstore Data Analytics Project
# -----------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set(style="whitegrid")

# 1️⃣ Load Dataset
df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

# 2️⃣ Basic Info
print("Dataset shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nSummary Info:")
print(df.info())

# 3️⃣ Check Missing Values
print("\nMissing values:\n", df.isnull().sum())

# 4️⃣ Basic Statistics
print("\nStatistical Summary:")
print(df.describe())

# 5️⃣ Total Sales and Profit
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
print(f"\n💰 Total Sales: {total_sales:,.2f}")
print(f"💹 Total Profit: {total_profit:,.2f}")

# 6️⃣ Sales by Category
plt.figure(figsize=(8,5))
sns.barplot(x="Category", y="Sales", data=df, estimator=sum, hue="Category", palette="viridis", legend=False)

plt.title("Total Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# 7️⃣ Profit by Region
plt.figure(figsize=(8,5))
sns.barplot(x="Region", y="Profit", data=df, estimator=sum, palette="coolwarm")
plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

# 8️⃣ Sales vs Profit Relationship
plt.figure(figsize=(8,5))
sns.scatterplot(x="Sales", y="Profit", hue="Category", data=df)
plt.title("Sales vs Profit by Category")
plt.tight_layout()
plt.show()

# 9️⃣ Top 10 States by Sales
top_states = df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_states.values, y=top_states.index, palette="magma")
plt.title("Top 10 States by Sales")
plt.xlabel("Total Sales")
plt.ylabel("State")
plt.tight_layout()
plt.show()

# 🔟 Ship Mode Preference
plt.figure(figsize=(6,4))
sns.countplot(x="Ship Mode", data=df, palette="pastel")
plt.title("Distribution of Ship Modes")
plt.tight_layout()
plt.show()

print("\n✅ Analysis Complete! Visualizations generated successfully.")
