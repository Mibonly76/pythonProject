from math import floor
amount_tournaments = int(input())
points = int(input())

total_points = 0
winnings = 0

for _ in range(amount_tournaments):
    position = input()
    if position == "W":
        total_points += 2000
        winnings += 1
    elif position == "F":
        total_points += 1200
    else:
        total_points += 720


avr_points = total_points / amount_tournaments
total_points += points
winnings /= amount_tournaments

print(f"Final points: {floor(total_points)}")
print(f"Average points: {floor(avr_points)}")
print(f"{winnings * 100:.2f}%")
