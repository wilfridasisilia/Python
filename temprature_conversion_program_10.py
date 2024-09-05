unit = input("Is this temprature in celcius or fahrenheit (F or C): ")
temp = float(input("Enter the temprature: "))

if unit == 'C' or unit == 'c':
    temp = round((9*temp)/5 + 32,1)
    print(f"The temprature in Fahrenheit is: {temp}F")
elif unit == 'F' or unit == 'f':
    temp = round((temp - 32)*5/9,1)
    print(f"The temprature in Celcius is: {temp}C")
else:
    print(f"{unit} is an invalid unit of measurement")