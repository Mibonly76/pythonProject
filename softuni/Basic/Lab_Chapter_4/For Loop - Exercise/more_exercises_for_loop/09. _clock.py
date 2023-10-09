hour = 0
minutes = 0
for _ in range(1440):
    print(f"{hour} : {minutes}")
    minutes += 1
    if minutes == 60:
        minutes = 0
        hour += 1
        if hour == 24:
            break
