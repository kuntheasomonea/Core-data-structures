inventory = {'coffee beans': 50, 'cups': 100, 'syrup': 15}
while True:
    print("\nCurrent inventory:", inventory)
    action = input("Do you want to 'sell', 'restock', or 'quit'? ").lower()
    if action == 'quit':
        print("Exiting the inventory manager.")
        break
    elif action == 'sell':
        item = input("Enter the item to sell: ").lower()
        if item in inventory:
            try:
                quantity = int(input(f"Enter quantity of {item} to sell: "))
                if quantity <= inventory[item]:
                    inventory[item] -= quantity
                    print(f"Sold {quantity} {item}(s).")
                else:
                    print("Not enough stock to sell that quantity!")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Item not found in inventory!")
    elif action == 'restock':
        item = input("Enter the item to restock: ").lower()
        if item in inventory:
            try:
                quantity = int(input(f"Enter quantity of {item} to add: "))
                inventory[item] += quantity
                print(f"Restocked {quantity} {item}(s).")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Item not found in inventory!")
    else:
        print("Invalid action! Please choose 'sell', 'restock', or 'quit'.")