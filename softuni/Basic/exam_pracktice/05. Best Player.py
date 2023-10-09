command = input()
score = int(input())
current_layer = command
current_score = score

while True:
    command = input()
    if command == "END" or current_layer == "END":
        break
    score = int(input())

    if current_score < score:
        current_layer = command
        current_score = score

    if current_score >= 10:
        break

print(f"{current_layer} is the best player!")
if current_score >= 3:
    print(f"He has scored {current_score} goals and made a hat-trick !!!")
elif 0 <= current_score < 3:
    print(f"He has scored {current_score} goals.")
