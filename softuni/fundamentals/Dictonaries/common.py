# keys = ["name", "age", "occupation"]
# values = ["Ilian", 47, "IT Manager"]
#
# person = {}
#
# for i in range(len(keys)):
#     key = keys[i]
#     value = values[i]
#     person[key] = value

# person = dict(name="Ilian", age=47, occupation="ITManager")

# person = dict([("name", "Ilian"), ("age", 47), ("occupation", "IT Manager")])

# keys = ["name", "age", "occupation"]
# values = ["Ilian", 47, "IT Manager"]
#
# person = dict(zip(keys, values))

person = {'name': 'Ilian',
          'age': 47,
          'occupation': 'IT Manager',
          "gpa": 6.00
          }

print(person["gpa"])
print(person.get("occupation"))
# print(person["address"])
print(person.get("address"))
person["class_number"] = 2
print(person.get("class_number"))
person["class_number"] += 1
print(person.get("class_number"))
person["class_number"] = str(person["class_number"]) + "A"
print(person.get("class_number"))

for key in person.keys():
    print(key, end=" ")
print()

for value in person.values():
    print(value, end=" ")
print()

for key in person.keys():
    print(person[key], end=" ")
print()

# ITEMS 

for key, value in person.items():
    print(key, value)

# person["gpa"] = [person["gpa"]]
#
# for _ in range(5):
#     gpa_value = float(input())
#     person["gpa"].append(gpa_value)
#     print(person)

if "name" in person.keys():
    print(person["name"])

if 6.0 in person.values():
    print("6.0 is available in the dictionary!")
