route = input().split("||")
fuel = int(input())
ammunition = int(input())

for command in route:
    tokens = command.split()
    action = tokens[0]
    if action == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
    value = int(tokens[1])

    if action == "Travel":
        if fuel >= value:
            fuel -= value
            print(f"The spaceship travelled {value} light-years.")
        else:
            print("Mission failed.")
            break

    elif action == "Enemy":
        enemy_armor = value
        if ammunition >= enemy_armor:
            ammunition -= enemy_armor
            print(f"An enemy with {enemy_armor} armour is defeated.")
        elif fuel >= 2 * enemy_armor:
            fuel -= 2 * enemy_armor
            print(f"An enemy with {enemy_armor} armour is outmaneuvered.")
        else:
            print("Mission failed.")
            break

    elif action == "Repair":
        ammunition_added = value * 2
        fuel_added = value
        ammunition += ammunition_added
        fuel += fuel_added
        print(f"Ammunitions added: {ammunition_added}.")
        print(f"Fuel added: {fuel_added}.")
