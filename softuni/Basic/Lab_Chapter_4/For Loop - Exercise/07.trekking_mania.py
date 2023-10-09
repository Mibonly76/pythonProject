amount_of_groups = int(input())

p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0
total_members = 0

for _ in range(amount_of_groups):
    number_of_members = int(input())
    total_members += number_of_members

    if number_of_members > 40:
        p5 += number_of_members
    elif 25 < number_of_members <= 40:
        p4 += number_of_members
    elif 12 < number_of_members <= 25:
        p3 += number_of_members
    elif 5 < number_of_members <= 12:
        p2 += number_of_members
    else:
        p1 += number_of_members

print(f"{p1 / total_members * 100:.2f}%")
print(f"{p2 / total_members * 100:.2f}%")
print(f"{p3 / total_members * 100:.2f}%")
print(f"{p4 / total_members * 100:.2f}%")
print(f"{p5 / total_members * 100:.2f}%")
