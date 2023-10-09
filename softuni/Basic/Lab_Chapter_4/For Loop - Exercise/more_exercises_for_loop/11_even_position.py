from sys import maxsize
numbers = int(input())
odd_sum = 0
even_sum = 0
odd_max_digit = -maxsize
odd_min_digit = maxsize
even_min_digit = maxsize
even_max_digit = -maxsize
odd_max_digit_str = "No"
odd_min_digit_str = "No"
even_max_digit_str = "No"
even_min_digit_str = "No"

for i in range(1, numbers + 1):
    digit = float(input())
    if i % 2 == 0:
        even_sum += digit
        if digit > even_max_digit:
            even_max_digit = digit
            even_max_digit_str = str(f"{even_max_digit:.2f}")
        if digit < even_min_digit:
            even_min_digit = digit
            even_min_digit_str = str(f"{even_min_digit:.2f}")

    else:
        odd_sum += digit
        if digit > odd_max_digit:
            odd_max_digit = digit
            odd_max_digit_str = str(f"{odd_max_digit:.2f}")
        if digit < odd_min_digit:
            odd_min_digit = digit
            odd_min_digit_str = str(f"{odd_min_digit:.2f}")

if odd_min_digit == "No" or odd_max_digit == "No":
    odd_max_digit_str = odd_min_digit_str = "No"

if even_min_digit == "No" or even_max_digit == "No":
    even_max_digit_str = even_min_digit_str = "No"

print(f"OddSum={odd_sum:.2f},")
print("OddMin=" + odd_min_digit_str + ",")
print("OddMax=" + odd_max_digit_str + ",")
print(f"EvenSum={even_sum:.2f},")
print("EvenMin=" + even_min_digit_str + ",")
print("EvenMax=" + even_max_digit_str)
