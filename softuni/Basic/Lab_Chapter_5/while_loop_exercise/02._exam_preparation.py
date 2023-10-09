number_of_bad_graduate = int(input())

average_score = 1
bad_counter = 0
graduate = 0
last_problem = None
total_score = 0
counter = 0

while bad_counter < number_of_bad_graduate:
    exercise = input()
    if exercise == "Enough":
        print(f"Average score: {average_score:.2f}")
        print(f"Number of problems: {counter}")
        print(f"Last problem: {last_problem}")
        break

    graduate = int(input())
    if graduate <= 4:
        bad_counter += 1
    total_score += graduate
    counter += 1
    average_score = total_score / counter
    last_problem = exercise
else:
    print(f"You need a break, {bad_counter} poor grades.")
