def shoot(aim_list, aim, shooting_power):
    if aim in range(len(aim_list)):
        if aim_list[aim] <= shooting_power:
            aim_list.pop(aim)
        else:
            aim_list[aim] -= shooting_power

    return aim_list


def add(aim_list, aim, shooting_power):
    if aim in range(len(aim_list)):
        aim_list.index(aim, shooting_power)
    else:
        print("Invalid placement!")
    return aim_list


def strike(aim_list, aim, shooting_radios):
    if aim - shooting_radios in range(len(aim_list)) and aim + shooting_radios in range(len(aim_list)):
        aim_list = aim_list[0:aim - shooting_radios] + aim_list[aim + shooting_radios + 1:]
    else:
        print("Strike missed!")
    return aim_list


targets = [int(target) for target in input().split()]

command = input()

while command != "End":

    command = command.split()
    command_instruction = command[0]
    if command_instruction == "Shoot":
        index = int(command[1])
        power = int(command[2])
        targets = shoot(targets, index, power)

    elif command_instruction == "Add":
        index = int(command[1])
        value = int(command[2])
        targets = add(targets, index, value)

    elif command_instruction == "Strike":
        index = int(command[1])
        radios = int(command[2])
        targets = strike(targets, index, radios)

    command = input()


targets = [str(element) for element in targets]
print("|".join(targets))
