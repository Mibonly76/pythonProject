def create_compositor_data(count_of_pieces):
    compositor_dict = {}
    for _ in range(count_of_pieces):
        piece, compositor, key = input().split("|")
        compositor_dict[piece] = {"composer": compositor, "tone": key}
    return compositor_dict


def add_to_compositor_dict(masterpiece, music, master, tone):
    if music not in masterpiece:
        masterpiece[music] = {"composer": master, "tone": tone}
        print(f"{music} by {master} in {tone} added to the collection!")
    else:
        print(f"{music} is already in the collection!")
    return masterpiece


def remove_to_compositor_dict(masterpiece, music):
    if music in masterpiece:
        del masterpiece[music]
        print(f"Successfully removed {music}!")
    else:
        print(f"Invalid operation! {music} does not exist in the collection.")
    return masterpiece


def change_key_to_compositor_dict(masterpiece, music, tone):
    if music in masterpiece:
        masterpiece[music]["tone"] = tone
        print(f"Changed the key of {music} to {tone}!")
    else:
        print(f"Invalid operation! {music} does not exist in the collection.")
    return masterpiece


def base_function(number_of_iterations):
    compositor_dict = create_compositor_data(number_of_iterations)
    while True:
        command = input()
        if command == "Stop":
            return compositor_dict

        elif command.startswith("Add"):
            run, piece, compositor, key = command.split("|")
            compositor_dict = add_to_compositor_dict(compositor_dict, piece, compositor, key)
        elif command.startswith("Remove"):
            run, piece = command.split("|")
            compositor_dict = remove_to_compositor_dict(compositor_dict, piece)
        elif command.startswith("ChangeKey"):
            run, piece, new_key = command.split("|")
            compositor_dict = change_key_to_compositor_dict(compositor_dict, piece, new_key)


number_of_pieces = int(input())
final_dict = base_function(number_of_pieces)
for print_key, value in final_dict.items():
    print(f"{print_key} -> Composer: {value['composer']}, Key: {value['tone']}")
