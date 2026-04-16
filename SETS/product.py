def input_products(prompt):
    products = input(prompt)
    # Convert input string to a set of trimmed product names (case-insensitive)
    return set(product.strip().lower() for product in products.split(','))

# Get sets of available and sold products
available_products = input_products("Enter available products (comma-separated): ")
sold_products = input_products("Enter sold products (comma-separated): ")

# Products still in stock: available but not sold out
in_stock = available_products.difference(sold_products)

# Products sold out: sold but no longer available
sold_out = sold_products.difference(available_products)

print("\nProducts still in stock:", in_stock)
print("Products sold out:", sold_out)
