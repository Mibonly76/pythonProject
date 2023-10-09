period = int(input())

doctors = 7
total_numbers_of_patients_checked = 0
total_unchecked_patients = 0

for day in range(1, period + 1):
    number_of_patients = int(input())
    if day % 3 == 0 and total_unchecked_patients > total_numbers_of_patients_checked:
        doctors += 1
    if number_of_patients > doctors:
        total_unchecked_patients += number_of_patients - doctors
        total_numbers_of_patients_checked += doctors
    else:
        total_numbers_of_patients_checked += number_of_patients

print(f"Treated patients: {total_numbers_of_patients_checked}.\nUntreated patients: {total_unchecked_patients}.")
