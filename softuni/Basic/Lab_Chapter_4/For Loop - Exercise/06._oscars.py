actor_name = input()
academy_points = float(input())
number_voters = int(input())

total_points = academy_points

for _ in range(number_voters):

    actor_voters_name = input()
    voters_point = float(input())

    length_of_name = len(actor_voters_name)
    total_points += ((length_of_name * voters_point) / 2)
    if total_points > 1250.50:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break
else:
    print(f"Sorry, {actor_name} you need {1250.50 - total_points:.1f} more!")
