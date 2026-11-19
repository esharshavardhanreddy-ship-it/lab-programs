
import csv
import matplotlib.pyplot as plt

# Create sales data
sales = [
    ["Product", "Quantity", "Price"],
    ["Laptop", 5, 50000],
    ["Mobile", 10, 20000],
    ["Tablet", 8, 15000],
    ["Headphones", 15, 2000],
    ["Keyboard", 12, 1000]
]

# Write data into CSV file
with open("sales.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(sales)

# Read CSV file
products = []
revenue = []

total_sales = 0

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["Product"]
        quantity = int(row["Quantity"])
        price = float(row["Price"])

        amount = quantity * price

        products.append(product)
        revenue.append(amount)

        total_sales += amount

# Display sales report
print("--- RETAIL SALES REPORT ---")

for i in range(len(products)):
    print(products[i], "Revenue:", revenue[i])

print("\nTotal Sales:", total_sales)

# Create bar chart
plt.bar(products, revenue)

plt.title("Retail Sales Dashboard")
plt.xlabel("Products")
plt.ylabel("Revenue (Rs.)")

plt.xticks(rotation=30)
plt.tight_layout()

plt.show()
