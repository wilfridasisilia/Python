# fruits = ["apple", "orange", "banana", "pineapple"],
# vegetables = ["celery", "carrots", "potatoes"]
# meats = ["chicken", "fish", "turkey"]

# groceries = [["apple", "orange", "banana", "pineapple"],
#              ["celery", "carrots", "potatoes"],
#              ["chicken", "fish", "turkey"]]
# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for col in row:
        print(col, end=" ")
    print()