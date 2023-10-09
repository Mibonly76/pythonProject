route = input().split("||")
fuel = int(input())
ammunition = int(input())


while True:
    for elements_in_bundle
    int_bundle = route[0].split()
    action = int_bundle[0]
    value = int(int_bundle[1])

    if action == "Travel":
        if fuel >= value:
            fuel -= value
            print(f"The spaceship traveled {value} light-years.")
        else:
            print("Mission failed.")
            break

    elif action == "Enemy":
        enemy_armour = value
        if ammunition >= enemy_armour:
            ammunition -= enemy_armour
            print(f"An enemy with {enemy_armour} armour is defeated.")
        elif fuel >= enemy_armour * 2:
            fuel -= enemy_armour * 2
            print(f"An enemy with {enemy_armour} armour is outmaneuvered.")
        else:
            print("Mission failed.")
            break

    elif action == "Repair":
        added_ammunition = value // 2
        added_fuel = value
        ammunition += added_ammunition
        fuel += added_fuel
        print(f"Ammunitions added: {added_ammunition}.")
        print(f"Fuel added: {added_fuel}.")

    elif action == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
