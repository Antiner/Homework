# Task 1.4
# Write a Python program to sort a dictionary by key.

def task_1_4(dictionary):
    for key in sorted(dictionary):
        print("%s: %s" % (key, dictionary[key]))
