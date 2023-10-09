hour = 0
minutes = 0
seconds = 0
for _ in range(86400):
    print(f"{hour} : {minutes} : {seconds}")
    seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1
            if hour == 24:
                break
