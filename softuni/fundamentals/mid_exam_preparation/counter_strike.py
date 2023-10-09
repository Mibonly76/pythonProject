initial_energy = int(input())
distance = input()

battle_won_counter = 0


while distance != "End of battle":

    distance = int(distance)

    if distance <= initial_energy > 0:
        initial_energy -= distance
        battle_won_counter += 1
        if battle_won_counter % 3 == 0:
            initial_energy += battle_won_counter
    else:
        print(f"Not enough energy! Game ends with {battle_won_counter} won battles and {initial_energy} energy")
        break
    distance = input()
else:
    print(f"Won battles: {battle_won_counter}. Energy left: {initial_energy}")
