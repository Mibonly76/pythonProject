number_loads = int(input())

total_load_weight = 0
total_truck_weight = 0
total_train_weight = 0
total_bus_weight = 0
train = 0
truck = 0
bus = 0

for _ in range(number_loads):
    weight_of_load = int(input())
    total_load_weight += weight_of_load

    if weight_of_load >= 12:
        train += weight_of_load
        total_train_weight = train
    elif 4 <= weight_of_load < 12:
        truck += weight_of_load
        total_truck_weight = truck
    else:
        bus += weight_of_load
        total_bus_weight = bus
bus *= 200
truck *= 175
train *= 120
average = bus / total_load_weight + truck / total_load_weight + train / total_load_weight

print(f"{average:.2f}"
      f"\n{total_bus_weight / total_load_weight * 100:.2f}%\n"
      f"{total_truck_weight / total_load_weight * 100:.2f}%\n"
      f"{total_train_weight / total_load_weight * 100:.2f}%")
