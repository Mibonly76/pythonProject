words_imput_list = input().split()
dictionary = {}

for word in words_imput_list:
    word_lowcase = word.lower()
    if word_lowcase not in dictionary:
        dictionary[word_lowcase] = 0
    dictionary[word_lowcase] += 1

for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")
