v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

v2 = (p1 * h) + (p2 * h)

if v >= v2:
    print(f"The pool is {v2 / v * 100:.2f}% full. "
          f"Pipe 1: {p1 * h / v2 * 100:.2f}%. Pipe 2: {p2 * h / v2 * 100:.2f}%.")
elif v < v2:
    print(f"For {h} hours the pool overflows with {v2 - v} liters.")
