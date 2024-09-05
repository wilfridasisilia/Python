# Conditioal Expression = A one-line shortcut for the if-else (ternary operstor)
# print or assign one of two values based on a condition
# x if condition else y

num = 5
a = 6
b = 7
age = 13
temprature = 20
user_role = "admin"
# x if condition else y
# result = "Even" if num % 2 == 0 else "Odd"
# print(result)
# print("Positive" if num > 0 else "Negative")

max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Child"
weather = "Hot" if temprature > 20 else "Cold"
access_level = "Full access" if user_role == 'admin' else 'Limited access'
print(access_level)