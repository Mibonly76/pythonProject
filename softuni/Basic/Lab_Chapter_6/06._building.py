flours = int(input())
apartments = int(input())

flat_type = " "

for i in range(flours, 0, -1):
    for y in range(apartments):
        if i == flours:
            flat_type = f"L{i}{y}"
        elif i % 2 == 0:
            flat_type = f"O{i}{y}"
        elif i % 2 != 0:
            flat_type = f"A{i}{y}"
        print(flat_type, end=" ")
    print()
