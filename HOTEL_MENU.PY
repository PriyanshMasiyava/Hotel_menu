# Define the menu of the cafe
menu = {
    'Cake': 120,
    'Pasta': 150,
    'Pizza': 250,
    'Croissant': 80,
    'Muffin': 60,
    'Coffee': 100,
    'Latte': 120,
    'Mocha': 130,
    'Sandwich': 90,
    'Burger': 150,
    'Fries': 80,
    'Nachos': 100,
    'Cheesecake': 140,
    'Cold Coffee': 110,
    'Red Velvet': 160
}

# Greet the customer
print("**** Welcome to Python Cafe ****")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

order_total = 0
order_list = []  # To store ordered items

# Loop for multiple orders
while True:
    item = input("\nEnter the name of the item you want to order (can complted order 'exit' ): ").strip()
    
    if item.lower() == "exit":
        break  # Exit ordering process
    
    if item in menu:
        order_total += menu[item]
        order_list.append(item)
        print(f"Your item {item} has been added to your order.")
    else:
        print(f"Sorry, {item} is not available.")

# Final order summary
if order_list:
    print("\n**** Order Summary ****")
    for ordered_item in order_list:
        print(f"{ordered_item}: Rs{menu[ordered_item]}")
    print(f"\nTotal amount to pay: Rs{order_total}")
else:
    print("\nNo items were ordered. Thank you for visiting!")

print("**** Thank you for visiting Python Cafe! ****")
