# For Loops = execute a block of code a fixed number of times.
#             you can iterate over a range, string, sequence, etc.

credit_card = "1234-5678-9012-3456"
for x in range(1, 21):
    if x == 13:
        continue #/break (berhenti di 12)
    else:
        print(x)

# for x in reversed(range(1, 11, 2)):
#     print(x)
# print("Happy New Year")