# Initialize empty list
customer_order = []
place_order = True

# Create Menu
menu_items = {
    1: {"Item name": "Burger", "Price": 4.99},
    2: {"Item name": "Hotdog", "Price": 3.99},
    3: {"Item name": "Fries", "Price": 2.99},
    4: {"Item name": "Soda", "Price": 1.99}
}
while place_order:
    # Print Menu
    print("Menu:")
    for key, item in menu_items.items():
        print(f"{key}. {item['Item name']} - ${item['Price']}")

    # Customer Selections
    while True:
        menu_selection = input("Enter the corresponding number of the item you would like to order: ")

        # Check if input is a number
        if not menu_selection.isdigit():
            print("Error: Please enter a valid number.")
        else:
            menu_selection = int(menu_selection)
            # Check if the selection is valid
            if menu_selection in menu_items:
                print(f"You selected {menu_items[menu_selection]['Item name']}.")
                break
            else:
                print("Error: The selected item does not exist in the menu.")

    menu_quantity = input("Please enter the number of the item you'd like to order (If entry is invalid, it will be set to 1): ")

    # Check if input is a number
    if not menu_quantity.isdigit():
        menu_quantity = 1
    else:
        menu_quantity = int(menu_quantity)

    # Store order
    customer_order.append({
        "Item": menu_items[menu_selection]['Item name'],
        "Quantity": menu_quantity,
        "Price per item": menu_items[menu_selection]['Price'],
        "Total price": menu_quantity * menu_items[menu_selection]['Price']
    })

    # Check to continue order
    while True:
        continue_ordering = input("Would you like to keep ordering? (y/n)").lower()
        if continue_ordering == 'y':
            print("We will keep ordering.")
            break
        elif continue_ordering == 'n':
            print("Thank you for ordering.")
            place_order = False
            break
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

# Print receipt
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# Loop through the customer order to print each line
for order in customer_order:
    item_name = order["Item"]
    quantity = order["Quantity"]
    price = order["Price per item"]

    # Calculate spaces needed for formatting
    item_space = " " * (26 - len(item_name)) 
    price_space = " " * (7 - len(f"${price:.2f}"))
    quantity_space = " " * (10 - len(str(quantity)))

    # Print the formatted line
    print(f"{item_name}{item_space}| ${price:.2f}{price_space}| {quantity}{quantity_space}")

# Calculate the total price using list comprehension
total_price = sum(order["Price per item"] * order["Quantity"] for order in customer_order)

# Display the total price to the customer
print(f"Total Price: ${total_price:.2f}")  
print(f"Enjoy your meal!")
