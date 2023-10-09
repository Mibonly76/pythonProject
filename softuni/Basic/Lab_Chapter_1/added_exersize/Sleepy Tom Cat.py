free_days = int(input())

work_days = 365 - free_days

play_on_work_day = work_days * 63
play_on_free_days = free_days * 127
common_time_to_play = play_on_free_days + play_on_work_day

if 30000 > common_time_to_play:
    difference = 30000 - common_time_to_play
    different_time_in_hour = difference // 60
    different_fime_in_minutes = difference % 60

    print("Tom sleeps well")
    print(f"{different_time_in_hour} hours and {different_fime_in_minutes} minutes less for play")

elif 30000 <= common_time_to_play:
    difference = common_time_to_play - 30000
    different_time_in_hour = difference // 60
    different_fime_in_minutes = difference % 60

    print("Tom will run away")
    print(f"{different_time_in_hour} hours and {different_fime_in_minutes} minutes more for play")
