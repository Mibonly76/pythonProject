rooms = int(input())

amount_of_free_seats = 0
missing_chair = False

for each_room in range(1, rooms + 1):
    seats_list = input().split(" ")
    if len(seats_list[0]) >= int(seats_list[1]):
        amount_of_free_seats += len(seats_list[0]) - int(seats_list[1])
    else:
        print(f"{int(seats_list[1]) - len(seats_list[0])} more chairs needed in room {each_room}")
        missing_chair = True

if not missing_chair:
    print(f"Game On, {amount_of_free_seats} free chairs left")
