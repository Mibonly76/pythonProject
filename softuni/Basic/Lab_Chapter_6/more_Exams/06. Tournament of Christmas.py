days = int(input())

counter = 1
WIN = 0
TOTAL_WINS = 0
TOTAL_LOSE = 0
LOSE = 0
SUM = 0
TOTAL = 0

for day in range(1, days + 1):
    while True:
        command = input()
        if command == "Finish":
            if WIN > LOSE:
                TOTAL += SUM * 1.1
            else:
                TOTAL += SUM
            SUM = 0
            WIN = 0
            LOSE = 0
            break
        if counter == 1:
            counter = 2
        else:
            if command == "win":
                WIN += 1
                SUM += 20
                TOTAL_WINS += 1
            elif command == "lose":
                LOSE += 1
                TOTAL_LOSE += 1
            counter = 1


if TOTAL_WINS > TOTAL_LOSE:
    print(f"You won the tournament! Total raised money: {TOTAL * 1.2:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {TOTAL:.2f}")
