# name = input("Enter your full name: ")
# phone_number = input("Enter your phone #: ")
#
# result = len(name)
# result = name.find("i")
# result = name.rfind("a") #reverse
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit() # true if only contains digit
# result = name.isalpha() # must be no space, all alphabeth
# result = phone_number.count("-")
# phone_number = phone_number.replace("-", " ")
#
#
# print(phone_number)
# print(name)
# print(result)


#### Validate user input exercise
#1. username is no more than 12 chara
#2. username must not contain spaces
#3. username must not contains digit

username = input("Enter a username: ")

if len(username)>12:
    print("Your username can't be more that 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contains spaces")
elif not username.isalpha():
    print("Your username can't contains numbers")
else:
    print(f"Welcome {username}")