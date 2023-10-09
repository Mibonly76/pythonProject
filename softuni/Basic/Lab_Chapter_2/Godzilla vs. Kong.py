budged = float(input())
amount_statist = int(input())
price_dress = float(input())

deco = budged * 0.1

if amount_statist > 150:
    price_dress *= 0.90

real_budged = (amount_statist * price_dress) + deco

if real_budged > budged:
    print("Not enough money!")
    print(f"Wingard needs {real_budged - budged:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budged - real_budged:.2f} leva left.")
