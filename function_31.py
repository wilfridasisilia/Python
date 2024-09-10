# function = a block of reusable code
# place () after the function name to invoke it

# def happy_birthday(name, age):
#     print(f"happy birthday {name}")
#     print(f"you are {age} years old")
#     print("god bless you")
#     print()
#
# happy_birthday("Bro", 19)
# happy_birthday("Frida", 20)

# def display_invoce(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")
# display_invoce("Brocode", 42.50, "01/01")

# return = statement used to end a function and send a result back to the caller
# def add(x, y):
#     z = x + y
#     return z
# print(add(2,3))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("wilfrida", "sisilia")
print(full_name)

