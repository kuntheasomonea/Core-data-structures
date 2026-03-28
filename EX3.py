cart_prices = []
while True:
    entry = input("Enter item price or 'done' to finish: ")
    if entry.lower() == 'done':
        break
    try:
        price = float(entry)
        cart_prices.append(price)
    except ValueError:
        print("Please enter a valid number or 'done' ")
total = sum(cart_prices)
max_price = max(cart_prices) if cart_prices else 0          
average = total / len(cart_prices) if cart_prices else 0

print("Total:", total)
print("Most expensive item:", max_price)
print("Average price:", average)