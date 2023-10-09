number_one = int(input())
number_two = int(input())


for numbers in range(number_one, number_two + 1):
    sum_odd = sum_even = 0
    for index, digit in enumerate(str(numbers)):
        if index % 2 == 0:
            sum_odd += int(digit)
        else:
            sum_even += int(digit)
    if sum_odd == sum_even:
        print(numbers, end=" ")
