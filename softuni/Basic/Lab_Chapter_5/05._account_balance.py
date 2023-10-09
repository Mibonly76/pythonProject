fee = input()
total = 0
while fee != "NoMoreMoney":
    fee = float(fee)
    if fee < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {fee:.2f}")
        total += fee
        fee = input()

print(f"Total: {total:.2f}")
