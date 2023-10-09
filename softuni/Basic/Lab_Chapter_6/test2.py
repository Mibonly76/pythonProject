for row in range(6):
    for col in range(21):
        if (row == 0 and col not in [4, 7, 8, 9, 10, 12, 15, 16, 17, 18]) \
            or (row == 1 and col not in [4, 5, 8, 11, 12, 15, 18])\
            or (row == 2 and col in [0, 1, 7, 8, 9, 13, 14, 16, 17, 19, 20]) \
            or (row == 3 and col in [0, 1, 7, 8, 13, 14, 16, 17, 19, 20]) \
            or (row == 4 and col not in [2, 3, 4, 5, 8, 9, 10, 11, 12]) \
            or (row == 5 and col not in [2, 3, 4, 5, 7, 8, 9, 10, 11, 12]):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()