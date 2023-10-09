n1 = int(input())
n2 = int(input())
operator = input()

result = 0
co_result = 0
even_or_odd = None


if operator == "+":
    result = n1 + n2

elif operator == "-":
    result = n1 - n2

elif operator == "*":
    result = n1 * n2

co_result = result % 2
if co_result == 0:
    even_or_odd = "even"
else:
    even_or_odd = "odd"

if operator == "+" or operator == "*" or operator == "-":
    print(f"{n1} {operator} {n2} = {result} - {even_or_odd}")
elif operator == "/" and n2 != 0:
    print(f"{n1} / {n2} = {n1 / n2:.2f}")
elif operator == "/" and n2 == 0:
    print(f"Cannot divide {n1} by zero")
elif operator == "%" and n2 == 0:
    print(f"Cannot divide {n1} by zero")
elif operator == "%":
    print(f"{n1} % {n2} = {n1 % n2}")
