the_speed = float(input())

if the_speed <= 10:
    print("slow")
elif 10 < the_speed <= 50:
    print("average")
elif 50 < the_speed <= 150:
    print("fast")
elif 150 < the_speed <= 1000:
    print("ultra fast")
else:
    print("extremely fast")
