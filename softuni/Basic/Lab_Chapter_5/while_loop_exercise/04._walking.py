STEPS_NEEDED = 10_000

steps_per_go = None
amount_of_steps = 0

while amount_of_steps < STEPS_NEEDED:
    steps_per_go = input()

    if steps_per_go == "Going home":

        amount_of_steps += int(input())
        break

    amount_of_steps += int(steps_per_go)

if amount_of_steps >= STEPS_NEEDED:
    print(f"Goal reached! Good job!\n{amount_of_steps - STEPS_NEEDED} steps over the goal!")
else:
    print(f"{STEPS_NEEDED - amount_of_steps} more steps to reach goal.")
