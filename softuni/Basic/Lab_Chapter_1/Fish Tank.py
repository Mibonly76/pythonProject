a = int(input())
b = int(input())
c = int(input())
percent_to_take = float(input())/100

a /= 10
b /= 10
c /= 10

volume = a * b * c

volume -= volume * percent_to_take

print(volume)
