def loot(entry_list, added_items):
    for items_in_list in added_items:
        if items_in_list not in entry_list:
            entry_list.insert(0, items_in_list)
    return entry_list


def drop(entry_list, action_index):
    if action_index < abs(len(entry_list)):
        entry_list.append(entry_list.pop(action_index))
    return entry_list


def steal(entry_list, action_index):
    if action_index >= len(entry_list):
        print(", ".join(entry_list))
        entry_list = []
    else:
        number_of_stolen_items = len(entry_list) - action_index
        print(", ".join(entry_list[number_of_stolen_items:]))
        entry_list = entry_list[:number_of_stolen_items]

    return entry_list


initial_loot = input().split("|")


command = input()

while command != "Yohoho!":

    command = command.split(" ")
    run_action = command[0]

    if run_action == "Loot":
        items = command[1:]
        initial_loot = loot(initial_loot, items)

    elif run_action == "Drop":
        index = int(command[1])
        initial_loot = drop(initial_loot, index)

    elif run_action == "Steal":
        element = int(command[1])
        initial_loot = steal(initial_loot, element)

    command = input()

else:
    if not len(initial_loot):
        print("Failed treasure hunt.")
    else:
        average_gain = sum(len(item) for item in initial_loot) / len(initial_loot)
        print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
