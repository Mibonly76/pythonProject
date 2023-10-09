words_list = input().split(" ")

for element_in_list in words_list:
    if len(element_in_list) % 2 == 0:
        print(element_in_list)
