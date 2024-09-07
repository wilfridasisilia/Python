# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates Ok.
# Set = {} unordered and immutable, but Add/Remove Ok. No duplicates.
# Tupple = () ordered and unchangeale. Duplicates Ok. Faster

# fruits = ["apple", "orange", "banana", "coconut"]
# print(dir(fruits))
# print(help(fruits))
# print(fruits[::-2])
# print(len(fruits))

# fruits[1] = "lemon"
# fruits.append("grape")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# fruits.append("banana")
# print(fruits.index("pineapple"))
# count_banana = fruits.count("banana")
# print(count_banana)
#
# for fruit in fruits:
#     print(fruit)

######################################

# fruits = {"apple", "orange", "banana", "coconut", "coconut"}
# fruits.add("pineapple")
# # fruits.remove("apple")
# fruits.pop()
# print(fruits)

########################################

fruits = ("apple", "orange", "banana", "coconut")
print(fruits.index("apple"))
print(fruits.count("coconut"))
for fruit in fruits:
    print(fruit)
.
