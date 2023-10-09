citty_name = input()
packet = input()
vip_or_not = input()
days = int(input())

if days < 1:
    print("Days must be positive number!")
    exit()

price = 0
folse_data = False

if citty_name == "Bansko" or citty_name == "Borovets":
    if packet == "withEquipment":
        if vip_or_not == "yes":
            price = 100 - 100 * 0.1
            price *= days
        else:
            price = days * 100
    elif packet == "noEquipment":
        if vip_or_not == "yes":
            price = 80 - 80 * 0.05
            price *= days
        else:
            price = days * 80
    else:
        folse_data = True

elif citty_name == "Varna" or citty_name == "Burgas":
    if packet == "withBreakfast":
        if vip_or_not == "yes":
            price = 130 - 130 * 0.12
            price *= days
        else:
            price = days * 130
    elif packet == "noBreakfast":
        if vip_or_not == "yes":
            price = 100 - 100 * 0.07
            price *= days
        else:
            price = days * 100
    else:
        folse_data = True
else:
    folse_data = True

if folse_data:
    print("Invalid input!")
else:
    print(f"The price is {price:.2f}lv! Have a nice time!")
