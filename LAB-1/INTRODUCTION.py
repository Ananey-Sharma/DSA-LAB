products = [
    (101, "Mobile", "Electronics", 20000),
    (102, "Laptop", "Electronics", 55000),
    (103, "Shoes", "Fashion", 3000),
    (104, "Watch", "Fashion", 2500),
    (105, "Headphones", "Electronics", 1500)
]

purchases = [
    ("User1", 101, 1),
    ("User2", 103, 2),
    ("User1", 102, 1),
    ("User3", 101, 1),
    ("User2", 105, 3)
]

searches = [
    "Mobile", "Shoes", "Mobile", "Laptop", "Mobile", "Watch"
]

# -------------------- Q1: Product Analysis --------------------
product_names = []
for product in products:
    product_names.append(product[1])

costliest_product = max(products, key=lambda x: x[3])

category_count = {}
for product in products:
    category = product[2]
    if category in category_count:
        category_count[category] += 1
    else:
        category_count[category] = 1

print("Outputs:")
print("Product Names:", product_names)
print("Costliest Product:", costliest_product)
print("Category Count:", category_count)

# -------------------- Q2: Purchase Analysis --------------------
user_total_items = {}
product_quantity = {}

for user, product_id, quantity in purchases:
    if user in user_total_items:
        user_total_items[user] += quantity
    else:
        user_total_items[user] = quantity

    if product_id in product_quantity:
        product_quantity[product_id] += quantity
    else:
        product_quantity[product_id] = quantity

top_user = max(user_total_items, key=user_total_items.get)

print("\nTotal Items Purchased by Each User:", user_total_items)
print("User who purchased the most items:", top_user)
print("Total Quantity Sold per Product:", product_quantity)

# -------------------- Q3: Revenue Calculation --------------------
price_dict = {}
for product in products:
    price_dict[product[0]] = product[3]

revenue_per_product = {}
total_revenue = 0

for product_id, quantity in product_quantity.items():
    revenue = price_dict[product_id] * quantity
    revenue_per_product[product_id] = revenue
    total_revenue += revenue

print("\nRevenue per Product:", revenue_per_product)
print("Total Store Revenue:", total_revenue)

# -------------------- Q4: Search Trend Analysis --------------------
search_count = {}

for item in searches:
    if item in search_count:
        search_count[item] += 1
    else:
        search_count[item] = 1

most_searched_product = max(search_count, key=search_count.get)

print("\nSearch Count:", search_count)
print("Most Searched Product:", most_searched_product)

# -------------------- Q5: Category Performance --------------------
product_category = {}
for product in products:
    product_category[product[0]] = product[2]

category_sales = {}

for product_id, quantity in product_quantity.items():
    category = product_category[product_id]

    if category in category_sales:
        category_sales[category] += quantity
    else:
        category_sales[category] = quantity

top_category = max(category_sales, key=category_sales.get)

print("\nItems Sold per Category:", category_sales)
print("Category with Highest Sales:", top_category)