# Logical Operator = evaluate multiple conditions (or, and, not)
# or = at least one condition must be true
# and = both conditions must be True
# not = inverts the condition (not false, not true)

# temp = -5
# is_raining = False
#
# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")

temp = 20
is_sunny = False

if temp >= 28 and is_sunny:
    print("It's Hot Outside")
    print("It's Sunny")
elif temp <= 0 and is_sunny:
    print("It's Cold Outside")
    print("It's Sunny")
elif 28 > temp > 0 and is_sunny:
    print("It's Warm Outside")
    print("It's Sunny")
elif temp >= 28 and not is_sunny:
    print("It's Hot Outside")
    print("It's Cloudy")
elif temp <= 0 and not is_sunny:
    print("It's Cold Outside")
    print("It's Cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("It's Warm Outside")
    print("It's Cloudy")