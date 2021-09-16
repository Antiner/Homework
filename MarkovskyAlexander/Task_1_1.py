# Task 1.1
# Write a Python program to calculate the length of a string without using the `len` function.

def task_1_1(n):
    count = 0
    for _ in str(n):
        count += 1
    print("Length of a string: ", count)
