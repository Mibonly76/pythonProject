price_for_vacation = float(input())
available_money = float(input())

following_days = 0
days_counter = 0

while following_days < 5:
    spend_or_save = input()
    sum_to = float(input())
    days_counter += 1
    if spend_or_save == "spend":
        available_money = available_money - sum_to if available_money > sum_to else 0
        following_days += 1
    else:
        available_money += sum_to
        following_days = 0

    if available_money >= price_for_vacation:
        print(f"You saved the money for {days_counter} days.")
        break

else:
    print(f"You can't save the money.\n{days_counter}")
