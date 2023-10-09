age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_given = 0
total_money = 0
total_toy_price = 0

for i in range(1, age + 1):

    if i % 2 == 0:
        money_given += 10
        total_money += money_given - 1

    else:
        total_toy_price += toy_price

if (total_toy_price + total_money) >= washing_machine_price:
    print(f"Yes! {(total_toy_price + total_money) - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - (total_toy_price + total_money):.2f}")
