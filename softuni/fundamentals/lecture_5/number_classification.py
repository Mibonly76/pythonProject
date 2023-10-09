list_of_numbers = [int(digit) for digit in (input().split(", "))]
list_of_positive = [str(positive_digits) for positive_digits in list_of_numbers if positive_digits >= 0]
list_of_negative = [str(negative_digits) for negative_digits in list_of_numbers if negative_digits < 0]
list_of_even = [str(even_digits) for even_digits in list_of_numbers if even_digits % 2 == 0]
list_of_odds = [str(odd_digits) for odd_digits in list_of_numbers if odd_digits % 2 != 0]

print_positive = ", ".join(list_of_positive)
print_negative = ", ".join(list_of_negative)
print_even = ", ".join(list_of_even)
print_odd = ", ".join(list_of_odds)

print(f"Positive: {print_positive}")
print(f"Negative: {print_negative}")
print(f"Even: {print_even}")
print(f"Odd: {print_odd}")
