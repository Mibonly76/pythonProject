dep_value = float(input())
dep_period = int(input())
yearly_percent = float(input())/100

fee_for_month = yearly_percent / 12

sum_amount = dep_value + dep_period * ((dep_value * yearly_percent)/12)

print(sum_amount)
