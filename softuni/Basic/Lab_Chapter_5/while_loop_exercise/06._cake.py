around = int(input()) * int(input())

amount_of_pieces = None

while True:
    amount_of_pieces = input()

    if amount_of_pieces == "STOP":
        break
    else:
        around -= int(amount_of_pieces)
        if around <= 0:
            break

if around > 0:
    print(f"{around} pieces are left.")
else:
    print(f"No more cake left! You need {abs(around)} pieces more.")
