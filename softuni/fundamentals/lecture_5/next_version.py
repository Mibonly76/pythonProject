version_list = [int(version_element) for version_element in (input().split("."))]
new_version_list = []
last_version_element = version_list[2] + 1
second_version_element = 0
first_version_element = 0


if last_version_element > 9:
    last_version_element = 0
    second_version_element = version_list[1] + 1
else:
    second_version_element = version_list[1]

if second_version_element > 9:
    second_version_element = 0
    first_version_element = version_list[0] + 1
else:
    first_version_element = version_list[0]

new_version_list.append(str(first_version_element))
new_version_list.append(str(second_version_element))
new_version_list.append(str(last_version_element))

print(".".join(new_version_list))
