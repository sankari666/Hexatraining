#Capstone project-1
#1
with open('orders.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    records = list(reader)

#2
for record in records:
    print(record)

#3
total_orders = len(records) - 1
print(total_orders)

#4
total_revenue = 0
for row in reader:
    quantity = int(row['Quantity'])
    price = float(row['Price'])
    revenue = quantity * price
    total_revenue += revenue
print(total_revenue)

#5
highest_order_value = 0
for row in reader:
    order_value = int(row['Quantity']) * float(row['Price'])
    if order_value > highest_order_value:
        highest_order_value = order_value
print(highest_order_value)

#6
lowest_order_value = float('inf')
for row in reader:
    order_value = int(row['Quantity']) * float(row['Price'])
    if order_value < lowest_order_value:
        lowest_order_value = order_value
print(lowest_order_value)

#7
total_order_value = 0
order_count = 0
for row in reader:
    order_value = int(row['Quantity']) * float(row['Price'])
    total_order_value += order_value
    order_count += 1
average_order_value = total_order_value / order_count
print(average_order_value)

#8
customers = set()
for row in reader:
    customers.add(row['Customer'])
for customer in customers:
    print(customer)

#9
print(len(customers))

#10
customer_totals = {}
for row in reader:
    customer = row['Customer']
    purchase_amount = int(row['Quantity']) * float(row['Price'])
    customer_totals[customer] = customer_totals.get(customer, 0) + purchase_amount
highest_customer = max(customer_totals, key=customer_totals.get)
print(highest_customer)
print(customer_totals[highest_customer])

#11
product_orders = {}
for row in reader:
    product = row['Product']
    product_orders[product] = product_orders.get(product, 0) + 1

for product, count in product_orders.items():
    print(product, ":", count)

#12
product_revenue = {}
for row in reader:
    product = row['Product']
    revenue = int(row['Quantity']) * float(row['Price'])
    product_revenue[product] = product_revenue.get(product, 0) + revenue

for product, revenue in product_revenue.items():
    print(product, ":", revenue)

#13
product_quantity = {}
for row in reader:
    product = row['Product']
    quantity = int(row['Quantity'])
    product_quantity[product] = product_quantity.get(product, 0) + quantity
most_sold = max(product_quantity, key=product_quantity.get)
print(most_sold)
print(product_quantity[most_sold])

#14
product_quantity = {}
for row in reader:
    product = row['Product']
    quantity = int(row['Quantity'])
    product_quantity[product] = product_quantity.get(product, 0) + quantity
least_sold = min(product_quantity, key=product_quantity.get)
print(least_sold)
print(product_quantity[least_sold])

#15
category_revenue = {}
for row in reader:
    category = row['Category']
    revenue = int(row['Quantity']) * float(row['Price'])
    category_revenue[category] = category_revenue.get(category, 0) + revenue

for category, revenue in category_revenue.items():
    print(category, ":", revenue)

#16
city_orders = {}
for row in reader:
    city = row['City']
    city_orders[city] = city_orders.get(city, 0) + 1

for city, count in city_orders.items():
    print(city, ":", count)

#17
city_revenue = {}
for row in reader:
    city = row['City']
    revenue = int(row['Quantity']) * float(row['Price'])
    city_revenue[city] = city_revenue.get(city, 0) + revenue

for city, revenue in city_revenue.items():
    print(city, ":", revenue)

#18
for row in reader:
    city = row['City']
    revenue = int(row['Quantity']) * float(row['Price'])
    city_revenue[city] = city_revenue.get(city, 0) + revenue
highest_city = max(city_revenue, key=city_revenue.get)

print(highest_city)
print(city_revenue[highest_city])

#19
products = []
for row in reader:
    products.append(row['Product'])
products.sort()

for product in products:
    print(product)

#20
cities = set()
for row in reader:
    cities.add(row['City'])

for city in cities:
    print(city)

#21
city_revenue = {}
for row in reader:
    city = row['City']
    revenue = int(row['Quantity']) * float(row['Price'])
    city_revenue[city] = city_revenue.get(city, 0) + revenue
print(city_revenue)

#22
product_quantity = {}
for row in reader:
    product = row['Product']
    quantity = int(row['Quantity'])
    product_quantity[product] = product_quantity.get(product, 0) + quantity
print(product_quantity)

#23
def calculate_total_revenue(filename):
    total_revenue=0
    for row in reader:
        total_revenue += int(row['Quantity']) * float(row['Price'])
    return total_revenue

#24
def find_top_product(filename):
    product_quantity = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            product = row['Product']
            quantity = int(row['Quantity'])
            product_quantity[product] = product_quantity.get(product, 0) + quantity
    return max(product_quantity, key=product_quantity.get)

#25
def find_top_city(filename):
    city_revenue = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            city = row['City']
            revenue = int(row['Quantity']) * float(row['Price'])
            city_revenue[city] = city_revenue.get(city, 0) + revenue
    return max(city_revenue, key=city_revenue.get)

#26
def find_average_order_value(filename):
    total_value = 0
    order_count = 0
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_value += int(row['Quantity']) * float(row['Price'])
            order_count += 1
    return total_value / order_count

#27
try:
    with open('orders.csv', 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(row)

except FileNotFoundError:
    print("Error: orders.csv file not found.")

#28
for row in reader:
        try:
            quantity = int(row['Quantity'])
            print("Quantity:", quantity)

        except ValueError:
            print("Invalid Quantity:", row['Quantity'])

#29
for row in reader:
        try:
            price = float(row['Price'])
            print("Price:", price)

        except ValueError:
            print("Invalid Price:", row['Price'])

#30
df = pd.read_csv("orders.csv")
order_values = np.array(df["Quantity"] * df["Price"])
print(np.sum(order_values))
print(np.mean(order_values))
print(np.max(order_values))
print(np.min(order_values))
print(np.std(order_values))

#31
df = pd.read_csv("orders.csv")
print(df.head())

#32
df["Revenue"] = df["Quantity"] * df["Price"]
print(df.head())

#33
top5 = df.sort_values(by="Revenue", ascending=False).head(5)
print(top5)

#34
city_revenue = df.groupby("City")["Revenue"].sum()
print(city_revenue)

#35
product_revenue = df.groupby("Product")["Revenue"].sum()
print(product_revenue)

#36
top_products = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
print(top_products)

#37
city_orders = df.groupby("City").size()
print(city_orders)

#38
high_value_orders = df[df["Revenue"] > 50000]

high_value_orders.to_csv(
    "high_value_orders.csv",
    index=False
)

#39
electronics_orders = df[
    df["Category"] == "Electronics"
]

electronics_orders.to_csv(
    "electronics_orders.csv",
    index=False
)

#40
df = pd.read_csv("orders.csv")
df["Revenue"] = df["Quantity"] * df["Price"]

while True:
    print("1. View Orders")
    print("2. Revenue Analysis")
    print("3. Product Analysis")
    print("4. City Analysis")
    print("5. Export Reports")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        print(df)

    elif choice == "2":
        print("Total Revenue:", df["Revenue"].sum())
        print("Average Revenue:", df["Revenue"].mean())
        print("Maximum Revenue:", df["Revenue"].max())
        print("Minimum Revenue:", df["Revenue"].min())

    elif choice == "3":
        print(
            df.groupby("Product")["Quantity"]
            .sum()
            .sort_values(ascending=False)
        )

    elif choice == "4":
        print(
            df.groupby("City")["Revenue"]
            .sum()
            .sort_values(ascending=False)
        )

    elif choice == "5":

        df.to_csv(
            "sales_export.csv",
            index=False
        )

        print("Report Exported")

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
