# Concession stand game

menu = {
    'pizza': 6.00,
    'burger': 3.75,
    'popcorn': 2.50,
    'fries': 1.50,
    'chips': 1.25,
    'soda': 1.00,
    'lemonade': 4.00
}

print('----- MENU -----')
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print('----------------')

cart = []
total = 0
while True:
    food = input("Select an item (q to quit): ")
    if food.lower() == 'q':
        break
    if menu.get(food):
        cart.append(food)
        total += menu.get(food)

print('----- YOUR ORDER -----')
print(', '.join(cart))
print(f"Total is ${total:.2f}")
