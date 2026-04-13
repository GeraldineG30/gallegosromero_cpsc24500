from menu_item import MenuItem
from order import Order

DRINKS = [
    ("Americano", 3.50),
    ("Cappuccino", 4.25),
    ("Espresso", 3.00),
    ("Latte", 4.75),
]

SIZES = [
    ("Small", 0.00),
    ("Medium", 0.75),
    ("Large", 1.25),
]

def show_drink_menu():
    print("\n**** Drink Menu ****")
    for i, (name, price) in enumerate(DRINKS, start=1):
        print(f"{i}. {name} - ${price:.2f}")

def show_size_menu():
    print("\n**** Size Menu ****")
    for i, (size, upcharge) in enumerate(SIZES, start=1):
        print(f"{i}. {size} (+${upcharge:.2f})")

def choose_drink():
    show_drink_menu()
    drink_choice = int(input("Choose a drink: "))
    drink_name, base_price = DRINKS[drink_choice - 1]

    show_size_menu()
    size_choice = int(input("Choose a size: "))
    size_name, upcharge = SIZES[size_choice - 1]

    price = base_price + upcharge

    return MenuItem(drink_name, size_name, price)

def main():
    print("*" * 47)
    print('%-15s %-15s %-15s' % ("*", "Starlight Coffee POS"))
    print("*" * 47)

    customer_name = input("Enter your name: ")
    order = Order(customer_name)

    # First Selection
    item = choose_drink()
    order.add_item(item)

    # Menu options
    while True:
        print("What would you like to do?")
        print("     1. Add anothe drink")
        print("     2. Remove a drink")
        print("     3. View order")
        print("     4. Check out")

        choice = input("Choice: ")

        if choice == "1":
            item = choose_drink()
            order.add_item(item)
        elif choice == "2":
            print(order)
            index = int(input("Enter item #number to remove: "))
            order.remove_item(index)
        elif choice == "3":
            print(order)
        elif choice == "4":
            print(order)
            print(f"Thank you, {customer_name}! Enjoy your Order")
            break
        else:
            print("Invalid selection, try again.")

if __name__ == "__main__":
    main()