import datetime

menu = {
    1 : { "name": "Burger", "price": 5.99, },

    3: { "name": "Salad", "price": 4.99 },
    4: { "name": "Drink", "price": 1.99 }
}

order = []
print("--- Welcome to Python Burgers! ---")


def display_menu_items():
    """Prints the menu items."""
    for x, details in menu.items():
        print(f"{x}. {details['name']}, ${details['price']:.2f}")

def take_orders():
    """Takes the user's order and adds it to the order list."""
    try:
        item_quantity = int(input("\n \t How many different items would you like to order? "))
        for i in range(item_quantity):
            item_number = int(input(f"\n \t Enter your choice #{i+1}? "))
            if item_number in menu:
                item_how_many = int(input(f"\t How many {menu[item_number]['name']}'s? "))
                
                ordered_item = {
                    "name": menu[item_number]["name"],
                    "price": menu[item_number]["price"],
                    "quantity": item_how_many
                }
                order.append(ordered_item)
            else:
                print("Invalid item number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def save_receipt_to_file(order_details, total_price):
     """Saves the final receipt to a text file."""
    # Generate a unique filename with a timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"receipt_{timestamp}.txt"
    
    try:
        with open(filename, 'w') as file:
            file.write("--- Python Burgers Receipt ---\n")
            file.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("-----------------------------\n")
            for item in order_details:
                item_total = item["quantity"] * item["price"]
                file.write(f" {item['quantity']}x {item['name']} = ${item_total:.2f}\n")
            file.write("-----------------------------\n")
            file.write(f" Total: ${total_price:.2f}\n")
            file.write("\nThank you for your order!\n")
        print(f"\nReceipt successfully saved to {filename}")
    except IOError:
        print(f"Error: Could not write receipt to file {filename}.")


# --- Main Program Loop ---
while True:
    print("\n +-+-+-+ Today's Menu +-+-+-+")
    display_menu_items()
    
    # Takes orders
    take_orders()
    
    order_again = input("\n Would you like to add more items? (Y/n): ")
    if order_again.lower() == 'n':
        break

# --- Final Receipt Calculation and Display ---
if order:
    print("\n--- Your Final Receipt ---")
    total = 0
    # Calculate the total price
    for item in order:
        item_total = item["quantity"] * item["price"]
        print(f" {item['quantity']}x {item['name']} = ${item_total:.2f}")
        total += item_total
    print("--------------------------")
    print(f" Total: ${total:.2f}")
    print("\n !!! Thank you for visiting Python Burgers. Have a great day !!! \n")

    # Save the receipt to a file
    save_receipt_to_file(order, total)
else:
    print("\nNo order was placed. Goodbye!")


