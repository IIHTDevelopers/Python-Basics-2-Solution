# 1. Function to check and return low-stock items
def get_low_stock_items(inventory, reorder_level):
    low_stock = [item for item, stock in inventory if stock < reorder_level]
    return low_stock

# 2. Function to calculate the total inventory value
def calculate_inventory_value(inventory, prices):
    total_value = sum(stock * prices[item] for item, stock in inventory if item in prices)
    return total_value

# 3. Function to find the most stocked item


# Dataset: Inventory (Item, Quantity) and Prices
inventory_data = [
    ("Laptop", 5),
    ("Mouse", 20),
    ("Keyboard", 12),
    ("Monitor", 3),
    ("USB Drive", 50)
]

item_prices = {
    "Laptop": 1000,
    "Mouse": 25,
    "Keyboard": 80,
    "Monitor": 300,
    "USB Drive": 15
}

# Use Functions
low_stock_items = get_low_stock_items(inventory_data, 10)
print(" Items to Restock:", low_stock_items)

total_inventory_value = calculate_inventory_value(inventory_data, item_prices)
print(" Total Inventory Value: $", total_inventory_value)


