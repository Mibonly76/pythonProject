moves = int(input())
score = 0
dig1 = 0
dig2 = 0
dig3 = 0
dig4 = 0
dig5 = 0
dig6 = 0

for _ in range(moves):
    digit = int(input())

    if 0 <= digit < 10:
        score += digit * 0.2
        dig1 += 1
    elif 10 <= digit < 20:
        score += digit * 0.3
        dig2 += 1
    elif 20 <= digit < 30:
        score += digit * 0.4
        dig3 += 1
    elif 30 <= digit < 40:
        score += 50
        dig4 += 1
    elif 40 <= digit <= 50:
        score += 100
        dig5 += 1
    else:
        score /= 2
        dig6 += 1

print(f"{score:.2f}")
print(f"From 0 to 9: {dig1 / moves * 100:.2f}%")
print(f"From 10 to 19: {dig2 / moves * 100:.2f}%")
print(f"From 20 to 29: {dig3 / moves * 100:.2f}%")
print(f"From 30 to 39: {dig4 / moves * 100:.2f}%")
print(f"From 40 to 50: {dig5 / moves * 100:.2f}%")
print(f"Invalid numbers: {dig6 / moves * 100:.2f}%")
