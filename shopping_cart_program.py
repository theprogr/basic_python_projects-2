items = []
prices = []

while True:
    item = input("Enter an item to buy (q to quit): ")
    if item.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of a {item}: $"))
        items.append(item)
        prices.append(price)

print("----- YOUR CART -----")
print(', '.join(items))
print(f"Your total price is ${sum(prices)}")
