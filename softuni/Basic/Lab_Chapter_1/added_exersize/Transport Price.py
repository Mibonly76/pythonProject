n = int(input())
period = input()

if n < 20:
    if period == "day":
        taxi_day_price = 0.70 + 0.79 * n
        print(f"{taxi_day_price:.2f}")
    elif period == "night":
        taxi_night_price = 0.70 + 0.90 * n
        print(f"{taxi_night_price:.2f}")
elif 20 <= n < 100:
    bus_price = 0.09 * n
    print(f"{bus_price:.2f}")
else:
    train_price = 0.06 * n
    print(f"{train_price:.2f}")
