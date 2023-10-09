for row in range(6):
    for col in range(7):
        if (row == 0 and col % 3 != 0) \
            or (1 <= row <= 2) \
            or (row == 3 and col % 6 != 0) \
            or (row == 4 and 2 <= col <= 4) \
            or (row + col == 8):
            print("*", end = "  ")
        else:
            print(" ", end = "  ")
    print()
    