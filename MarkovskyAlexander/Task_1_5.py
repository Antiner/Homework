# Task 1.5
# Write a Python program to print all unique values of all dictionaries in a list.

def task_1_5(array):
    list_1 = []
    for i in array:
        for v in i:
            list_1.append(i.get(v))
    print(set(list_1))