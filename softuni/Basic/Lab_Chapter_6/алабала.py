destination = input()


while destination != "End":
    holiday_money = float(input())
    total_saved_money = 0

    while total_saved_money < holiday_money:
        money = float(input())
        total_saved_money += money
    else:
        print(f"Going to {destination}!")

    destination = input()
