class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price, quantity):
        if item_name in self.items:
            self.items[item_name][1] += quantity
        else:
            self.items[item_name] = [price, quantity]

    def view_cart(self):
        print("Items in your cart:")
        total_cost = 0
        for item_name, (price, quantity) in self.items.items():
            total_item_cost = price * quantity
            print(f"{item_name} - Quantity: {quantity}, Price per item: ${price:.2f}, Total: ${total_item_cost:.2f}")
            total_cost += total_item_cost
        print(f"Total cost: ${total_cost:.2f}")

def main():
    cart = ShoppingCart()

    while True:
        print("\nMenu:")
        print("1. Add item to cart")
        print("2. View cart")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            item_name = input("Enter item name: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            cart.add_item(item_name, price, quantity)
            print("Item added to cart.")

        elif choice == "2":
            cart.view_cart()

        elif choice == "3":
            print("Exiting. Thank you for using the shopping cart!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

