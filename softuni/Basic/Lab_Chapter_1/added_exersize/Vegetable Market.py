pv = float(input())
pf = float(input())
av = int(input())
af = int(input())

total_price = pf * af + pv * av
convert_in_euro = total_price / 1.94

print(f"{convert_in_euro:.2f}")
