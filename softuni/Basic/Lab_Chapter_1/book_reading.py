amount_of_pages = int(input())
amount_of_read_pages_per_hour = int(input())
amount_of_days = int(input())

all_time_for_reading_of_a_book = amount_of_pages // amount_of_read_pages_per_hour
hour_per_day = all_time_for_reading_of_a_book // amount_of_days

print(hour_per_day)
