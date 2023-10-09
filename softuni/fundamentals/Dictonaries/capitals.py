country_list = input().split(", ")
city_list = input().split(", ")

join_dict = dict(zip(country_list, city_list))

for key, value in join_dict.items():
    print(f"{key} -> {value}")
