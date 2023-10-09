x = float(input())
y = float(input())
h = float(input())

GREEN = 3.40
RED = 4.30

roof_area = (x * y * 2) + (x * h)

wall_area_one = (x * x) - 2.4
wall_area_two = x * x
wall_side_area = x * y - 2.25
wall_area = \
    (wall_side_area * 2) + \
    wall_area_one + \
    wall_area_two

print(f"{wall_area / GREEN:.2f}")
print(f"{roof_area / RED:.2f}")
