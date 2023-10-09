n = int(input())
salary = int(input())

for _ in range(n):
    tab = input()
    if tab == "Facebook":
        salary -= 150
    elif tab == "Instagram":
        salary -= 100
    elif tab == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break
else:
    print(salary)
