hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrive = int(input())
minutes_of_arrive = int(input())

difference = 0
hh = 0
mm = 0
convert_exam_hour = (hour_of_exam * 60) + minutes_of_exam
convert_arrive_hour = (hour_of_arrive * 60) + minutes_of_arrive

if convert_exam_hour >= convert_arrive_hour:
    difference = (convert_exam_hour - convert_arrive_hour)
    if convert_arrive_hour == convert_exam_hour or difference <= 30:
        print("On time")
    elif (convert_exam_hour - convert_arrive_hour) > 30:
        print("Early")

    if difference < 60 and difference != 0:
        print(f"{difference} minutes before the start")
    elif difference >= 60:
        hh = difference // 60
        mm = difference % 60
        print(f"{hh}:{mm:02d} hours before the start")
else:
    difference = (convert_arrive_hour - convert_exam_hour)
    print("Late")
    if difference < 60 and difference != 0:
        print(f"{difference} minutes after the start")
    elif difference >= 60:
        hh = difference // 60
        mm = difference % 60
        print(f"{hh}:{mm:02d} hours after the start")
