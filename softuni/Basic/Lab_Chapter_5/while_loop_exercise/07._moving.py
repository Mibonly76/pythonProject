amount = int(input()) * int(input()) * int(input())

amount_of_boxes = None

while True:
    amount_of_boxes = input()

    if amount_of_boxes == "Done":
        break
    else:
        amount -= int(amount_of_boxes)
        if amount < 0:
            break

if amount >= 0:
    print(f"{amount} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(amount)} Cubic meters more.")
