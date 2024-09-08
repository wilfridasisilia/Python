# Dictionary = a collection of {key:value} pairs
# ordered and changeable, no duplicates

capitals = {"USA" : "Washington DC",
            "India" : "New Delhi",
            "China" : "Beijing",
            "Russia" : "Moscow"}
# print(dir(capitals))
# print(capitals.get("USA"))
if capitals.get("China"):
    print("That capital exists")
else:
    print("That capital is not exists")

capitals.update({"Germany" : "Berlin"})
capitals.update({"USA" : "Detroit"})
capitals.pop("China")
capitals.popitem() #remove the leastest item
# capitals.clear()
keys = capitals.keys()
print(keys)

# for key in capitals.keys():
#     print(key)

# for value in capitals.values():
#     print(value)

items = capitals.items()
for key, value in items:
    print(f"{key}: {value}")
# print(items)


print(capitals)

