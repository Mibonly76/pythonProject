hour = int(input())
minutes = int(input()) + 15

if minutes > 59:
    minutes -= 60
    hour += 1

if hour > 23:
    hour -= 24

print(f"{hour}:{minutes:02d}")
