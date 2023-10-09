type_of_fuel = input()
amount_of_fuel = float(input())
club_card = input()

GASOLINE = 2.22
DIESEL = 2.33
GAS = 0.93

total_price = 0.00
discount1 = 0.00

if type_of_fuel == "Gasoline":
    total_price = GASOLINE * amount_of_fuel
    if club_card == "Yes":
        discount1 = amount_of_fuel * 0.18
        total_price -= discount1
elif type_of_fuel == "Diesel":
    total_price = DIESEL * amount_of_fuel
    if club_card == "Yes":
        discount1 = amount_of_fuel * 0.12
        total_price -= discount1
elif type_of_fuel == "Gas":
    total_price = GAS * amount_of_fuel
    if club_card == "Yes":
        discount1 = amount_of_fuel * 0.08
        total_price -= discount1

if 20 <= amount_of_fuel <= 25:
    total_price *= 0.92
elif amount_of_fuel > 25:
    total_price *= 0.90

print(f"{total_price:.2f} lv.")
