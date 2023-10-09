number = int(input())

star = 0
dash = 0

left_right = (number - 1) // 2

# Top Part
for row in range((number + 1) // 2):
    if row % 2 == 0:
        print("_" * left_right, end="")
        print("*", end="")

        mid = number - 2 * left_right - 2
        
        if mid >= 0:
            print("_" * mid, end="")
            print("*", end="")
        print("_" * left_right)

    else:
        print("_" * left_right, end="")
        print("*", end="")
        print("*", end="")
        print("_" * left_right)
