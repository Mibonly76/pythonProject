t_shirt_price = float(input())
sum_for_ball = float(input())

shorts = t_shirt_price * 0.75
socks = shorts * 0.20
middle_sum_of_socks_and_t_shirt = t_shirt_price + shorts
buttnons_shues = 2 * middle_sum_of_socks_and_t_shirt

total_sum = buttnons_shues + socks + shorts + t_shirt_price
total_sum_with_dicount = total_sum - total_sum * 0.15

if total_sum_with_dicount >= sum_for_ball:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_sum_with_dicount:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {sum_for_ball - total_sum_with_dicount:.2f} lv. more.")
