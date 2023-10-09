text = input()

SUM = 0

for let in text:

    if let == "a":
        SUM += 1
    elif let == "e":
        SUM += 2
    elif let == "i":
        SUM += 3
    elif let == "o":
        SUM += 4
    elif let == "u":
        SUM += 5
    else:
        continue

print(SUM)
