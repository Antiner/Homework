# Task 1.2
# Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).

def task_1_2(string):
    dictionary = {}

    for n in str(string):
        keys = dictionary.keys()
        if n in keys:
            dictionary[n] += 1
        else:
            dictionary[n] = 1
    print(dictionary)
