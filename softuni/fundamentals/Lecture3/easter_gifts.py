gifts_list = []
temp_list = []
position = 0
stop_put_in_gift_list = False
while True:
    command_list = []
    gift_name = input()
    if gift_name == "No Money":
        break
    command_list = gift_name.split(" ")

    if "OutOfStock" in command_list:
        stop_put_in_gift_list = True
        item = command_list[1]
        while True:
            if item in gifts_list:
                position = gifts_list.index(item)
                gifts_list.insert(position, "None")
                gifts_list.remove(item)
            else:
                break
    elif "Required" in command_list:
        stop_put_in_gift_list = True
        index_gift = command_list[1]
        index_value = int(command_list[2])
        if 0 > index_value + 1 or index_value + 1 > len(gifts_list):
            continue
        del gifts_list[index_value]
        gifts_list.insert(index_value, index_gift)
    elif "JustInCase" in command_list:
        stop_put_in_gift_list = True
        last_gift = command_list[1]
        del gifts_list[-1]
        gifts_list.append(last_gift)

    else:
        if stop_put_in_gift_list is False:
            stop_put_in_gift_list = True
            gifts_list = gift_name.split()


while True:
    if "None" in gifts_list:
        gifts_list.remove("None")
    else:
        break

print(*gifts_list)
