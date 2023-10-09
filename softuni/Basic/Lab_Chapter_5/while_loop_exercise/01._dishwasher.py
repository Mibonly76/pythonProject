amount_detergent = int(input()) * 750

DETERGENT_FOR_ONE_PLATE = 5
DETERGENT_FOR_ONE_POT = 15
COUNTER = 0
PLATES = 0
POTS = 0

while amount_detergent >= 0:
    dishes = input()
    if dishes == "End":
        print("Detergent was enough!")
        print(f"{PLATES} dishes and {POTS} pots were washed.")
        print(f"Leftover detergent {amount_detergent} ml.")
        break
    if COUNTER < 2:
        amount_detergent -= DETERGENT_FOR_ONE_PLATE * int(dishes)
        COUNTER += 1
        PLATES += int(dishes)

    else:
        amount_detergent -= DETERGENT_FOR_ONE_POT * int(dishes)
        COUNTER = 0
        POTS += int(dishes)

else:
    print(f"Not enough detergent, {abs(amount_detergent)} ml. more necessary!")
