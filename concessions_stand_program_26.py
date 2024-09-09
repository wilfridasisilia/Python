#   Concession Stand Program

menu = {"popcorn" : 1.00,
        "hot Dog" : 2.00,
        "giant pretzel" : 2.00,
        "asst candy" : 1.00,
        "soda" : 1.00,
        "lemonade" : 4.25}
cart = []
total = 0
print("--------Menu--------------")
for key, value in menu.items():
    print(f"{key:20}: ${value:.2f}")
print("--------Menu--------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------your order------------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")