from string import ascii_lowercase, ascii_uppercase, punctuation, digits
import random

length_of_password = int(input("Enter the length of the password: "))

# include_punctuations = punctuation
# include_low_case = ascii_lowercase
# include_upper_case = ascii_uppercase

include_low_case = input("Include low case? Yes or No? Default is Yes!: ")
include_upper_case = input("Include upper case? Yes or No? Default is Yes!: ")
include_punctuations = input("Include punctuations? Yes or No? Default is Yes!: ")

if include_low_case == "Yes":
    include_low_case = ascii_lowercase


if include_upper_case == "Yes":
    include_upper_case = ascii_uppercase


if include_punctuations == "Yes":
    include_punctuations = punctuation

sign_combination = digits + include_low_case + include_upper_case + include_punctuations
password_generator = ''.join(random.sample(sign_combination, length_of_password))

print(f"Your Password is: {password_generator}")
