tour_stops = input()

while True:
    command, *pattern = input().split(":")
    if command == "Travel":
        break

    if command == "Add Stop":
        index, string = pattern
        index = int(index)
        if 0 <= index < len(tour_stops):
            tour_stops = tour_stops[:index] + string + tour_stops[index:]

    elif command == "Remove Stop":
        start_index, stop_index = pattern
        start_index = int(start_index)
        stop_index = int(stop_index)
        if 0 <= start_index <= stop_index < len(tour_stops):
            tour_stops = tour_stops[:start_index] + tour_stops[stop_index + 1:]

    elif command == "Switch":
        old_str, new_str = pattern
        while old_str in tour_stops:
            tour_stops = tour_stops.replace(old_str, new_str)

    print(tour_stops)

print(f"Ready for world tour! Planned stops: {tour_stops}")