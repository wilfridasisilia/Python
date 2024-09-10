# keyword arguments = an argument preceded by an identifier helps with readability
# order of arguments doesnt matter
# 1. positional, 2. default, 3. keyword, 4. arbitary

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first} {last}")
#
# hello("Hello", title="Mr.", first="Spongebob", last="Squarepants")

# for x in range(1, 11):
#     print(x, end=" ")

# print("1", "2", "3", sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=1, area=234, first=567, last=890)
print(phone_num)
