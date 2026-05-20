import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import numpy as np

# Load data (correct path)
df = pd.read_csv(
    r"C:\Users\sambh\OneDrive\Desktop\Shopify-Data-Analysis-Project\data\raw_data.csv"
)


# =========================
# STEP 5: Data Cleaning + Export
# =========================

# 1. Copy data
clean_df = df.copy()

# 2. Remove duplicates
clean_df = clean_df.drop_duplicates()

# 3. Handle missing values
clean_df = clean_df.dropna()

# 4. Fix date format
clean_df["Invoice Date"] = pd.to_datetime(clean_df["Invoice Date"], errors='coerce')

# 5. Remove negative or zero sales
clean_df = clean_df[clean_df["Total Price Usd"] > 0]

# 6. Reset index
clean_df = clean_df.reset_index(drop=True)

# 7. Save cleaned file
clean_df.to_csv(
    r"C:\Users\sambh\OneDrive\Desktop\Shopify-Data-Analysis-Project\data\cleaned_data.csv",
    index=False
)

print("✅ cleaned_data.csv created successfully")


                                  # =========================
                                          # KPI Metrics
                                  # =========================

total_sales = df["Total Price Usd"].sum()

total_orders = df["Order Number"].nunique()

total_customers = df["Customer Id"].nunique()

avg_order_value = total_sales / total_orders

total_quantity = df["Quantity"].sum()

print("\n========== KPI METRICS ==========")

print(f"Total Sales Revenue : ${total_sales:,.2f}")

print(f"Total Orders : {total_orders}")

print(f"Total Customers : {total_customers}")

print(f"Average Order Value : ${avg_order_value:,.2f}")

print(f"Total Quantity Sold : {total_quantity}")

print("=================================\n")


                                      # =========================
                                        # Customer Segmentation
                                      # =========================

customer_data = df.groupby("Customer Id")["Total Price Usd"].sum().reset_index()

# KMeans clustering
kmeans = KMeans(
    n_clusters=3,
    random_state=42
)

customer_data["Cluster"] = kmeans.fit_predict(
    customer_data[["Total Price Usd"]]
)

# Plot
plt.figure(figsize=(10,5))

sns.scatterplot(
    data=customer_data,
    x=customer_data.index,
    y="Total Price Usd",
    hue="Cluster",
    palette="Set1"
)

plt.title("Customer Segmentation")

plt.tight_layout()

plt.savefig(
    r"C:\Users\sambh\OneDrive\Desktop\Shopify-Data-Analysis-Project\python\screenshots\customer_segmentation.png"
)

plt.close()


# =========================
# Monthly Sales Analysis
# =========================

df["Invoice Date"] = pd.to_datetime(
    df["Invoice Date"],
    errors="coerce"
)

# Extract Month
df["Month"] = df["Invoice Date"].dt.month

# Monthly Sales
monthly_sales = df.groupby("Month")["Total Price Usd"].sum()

print(monthly_sales)




# =========================
# Sales Prediction
# =========================

monthly_sales_df = monthly_sales.reset_index()

X = monthly_sales_df[["Month"]]

y = monthly_sales_df["Total Price Usd"]

model = LinearRegression()

model.fit(X, y)

future_months = np.array([[13], [14], [15]])

predictions = model.predict(future_months)

print("\n========== FUTURE SALES PREDICTION ==========")

for i, pred in enumerate(predictions):
    print(f"Month {13+i} Predicted Revenue = ${pred:,.2f}")

print("============================================")


# =========================
# Prediction Graph
# =========================

future_months_flat = [13, 14, 15]

plt.figure(figsize=(10,5))

# Original data
plt.plot(
    monthly_sales_df["Month"],
    monthly_sales_df["Total Price Usd"],
    marker='o',
    linewidth=3,
    label="Actual Sales"
)

# Predicted data
plt.plot(
    future_months_flat,
    predictions,
    marker='o',
    linewidth=3,
    linestyle='dashed',
    label="Predicted Sales"
)

plt.title("Sales Forecast Prediction")

plt.xlabel("Month")

plt.ylabel("Revenue")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig(
    r"C:\Users\sambh\OneDrive\Desktop\Shopify-Data-Analysis-Project\python\screenshots\sales_prediction.png"
)

plt.show()


                                      # =========================
                                        # Graph 1: Product Sales
                                      # =========================


# Group data
product_sales = df.groupby("Product Type")["Total Price Usd"].sum().sort_values(ascending=False)

# Dark theme
plt.style.use("dark_background")

# Plot
plt.figure(figsize=(10,5))
product_sales.plot(kind="bar", color="lime")

plt.title("Net Sales by Product Type")
plt.xticks(rotation=45)

# Save image
plt.tight_layout()
plt.savefig(r"C:..\Shopify-Data-Analysis-Project\python\screenshots\product_sales.png")

plt.close()




                                        # =========================
                                # Graph 2: Payment Method (Donut Chart)
                                       # =========================

payment_data = df["Gateway"].value_counts()

plt.figure(figsize=(8,6))

# Donut chart
plt.pie(payment_data, labels=payment_data.index, autopct='%1.1f%%', startangle=90)

# Circle for donut shape
centre_circle = plt.Circle((0,0),0.70,fc='black')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("Payment Method Distribution")

# Save image
plt.savefig(r"C:..\Shopify-Data-Analysis-Project\python\screenshots\payment_method.png")

plt.close()


                                       # =========================
                                         # Graph 3: Sales Trend
                                        # =========================

# Date convert
df["Invoice Date"] = pd.to_datetime(df["Invoice Date"])

# Group by date
sales_trend = df.groupby("Invoice Date")["Total Price Usd"].sum()

# Plot
plt.figure(figsize=(10,5))
sales_trend.plot(kind="line", linewidth=2)

plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue")

plt.tight_layout()

# Save image
plt.savefig(r"C:..\Shopify-Data-Analysis-Project\python/screenshots/sales_trend.png")

plt.close()



                                     # =========================
                                     # Graph 4: Top Cities by Sales
                                     # =========================

top_cities = df.groupby("CITY")["Total Price Usd"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_cities.plot(kind="bar", color="cyan")

plt.title("Top 10 Cities by Sales")
plt.xlabel("City")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

# Save image
plt.savefig(r"C:..\Shopify-Data-Analysis-Project\/python/screenshots/top_cities.png")

plt.close()


                                      # =========================
                                        # Graph 5: Top Customers
                                      # =========================

top_customers = df.groupby("Customer Id")["Total Price Usd"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_customers.plot(kind="bar", color="orange")

plt.title("Top 10 Customers by Spending")
plt.xlabel("Customer ID")
plt.ylabel("Total Spend")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig(r"C:..\Shopify-Data-Analysis-Project/python/screenshots/top_customers.png")
plt.close()


                                      # =========================
                                      # Graph 6: Country-wise Sales
                                      # =========================

country_sales = df.groupby("Billing Address Country")["Total Price Usd"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))
country_sales.plot(kind="bar", color="green")

plt.title("Sales by Country")
plt.xlabel("Country")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(r"C:..\Shopify-Data-Analysis-Project/python/screenshots/country_sales.png")
plt.close()


                                  # =========================
                                   # Graph 7: Monthly Sales
                                  # =========================

# Extract month
df["Invoice Date"] = pd.to_datetime(
    df["Invoice Date"],
    errors="coerce"
)
# Remove invalid dates
df["Month"] = df["Invoice Date"].dt.month
# df["Month"] = df["Invoice Date"].dt.month

monthly_sales = df.groupby("Month")["Total Price Usd"].sum()

plt.figure(figsize=(10,5))

monthly_sales.plot(
    kind="line",
    marker="o",
    linewidth=3,
    color="yellow"
)

plt.title("Monthly Sales Analysis")

plt.xlabel("Month")

plt.ylabel("Revenue")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    r"C:\Users\sambh\OneDrive\Desktop\Shopify-Data-Analysis-Project\python\screenshots\monthly_sales.png"
)

plt.close()

                                         # =========================
                                         # Graph 8: Correlation Heatmap
                                         # =========================

numeric_df = df.select_dtypes(include=['int64', 'float64'])

plt.figure(figsize=(10,6))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig(
    r"C:\Users\sambh\OneDrive\Desktop\Shopify-Data-Analysis-Project\python\screenshots\heatmap.png"
)

plt.close()