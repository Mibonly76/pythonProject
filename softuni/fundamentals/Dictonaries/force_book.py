
user_side_list = {}
side_user_list = {}


while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if " | " in command:
        command = command.split(" | ")
        force_user, force_side = command
        if force_side not in side_user_list.keys() and force_user not in side_user_list.values():
            side_user_list[force_side] = []
            side_user_list[force_side].append(force_user)
        elif force_user not in side_user_list.values() and force_side in side_user_list.keys():
            side_user_list[force_side].append(force_user)
    elif " -> " in command:
        command = command.split(" -> ")
        force_user, force_side = command
        if force_side not in user_side_list.keys() and force_user not in user_side_list.values():
            user_side_list[force_side] = []
            user_side_list[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")
        elif force_user not in user_side_list.values() and force_side in user_side_list.keys():
            user_side_list[force_side].append(force_user)
        elif force_user in user_side_list.values():
            user_side_list.pop(force_user)
            user_side_list[force_side].append(force_user)

print(user_side_list)
print(side_user_list)
