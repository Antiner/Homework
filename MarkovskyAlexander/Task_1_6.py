# Task 1.6
# Write a Python program to convert a given tuple of positive integers into an integer.

def task_1_6(nums):
    result = int(''.join(map(str, nums)))
    return result