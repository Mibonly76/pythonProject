record_in_seconds = float(input())
distance_in_meters = float(input())
time_for_one_m_in_seconds = float(input())

flat_time = distance_in_meters // 15 * 12.5

real_time = (distance_in_meters * time_for_one_m_in_seconds) + flat_time

if real_time < record_in_seconds:
    print(f" Yes, he succeeded! The new world record is {real_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {real_time - record_in_seconds:.2f} seconds slower.")
