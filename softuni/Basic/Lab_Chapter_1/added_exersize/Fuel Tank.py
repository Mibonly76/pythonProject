type_fuel = input()
amount_fuel = float(input())

if type_fuel == "Diesel":
    type_fuel = "diesel"
elif type_fuel == "Gasoline":
    type_fuel = "gasoline"
elif type_fuel == "Gas":
    type_fuel = "gas"

if type_fuel == "diesel" or type_fuel == "gasoline" or type_fuel == "gas":
    if amount_fuel >= 25:
        print(f"You have enough {type_fuel}.")
    else:
        print(f"Fill your tank with {type_fuel}!")
else:
    print("Invalid fuel!")
