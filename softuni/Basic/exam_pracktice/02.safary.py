budged = float(input())
gaz = float(input())
total_fee = gaz * 2.10 + 100
day = input()

if day != "Sunday":
    total_price = total_fee - total_fee * 0.1
else:
    total_price = total_fee - total_fee * 0.2

if total_price <= budged:
    print(f"Safari time! Money left: {budged - total_price:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {total_price - budged:.2f} lv.")
