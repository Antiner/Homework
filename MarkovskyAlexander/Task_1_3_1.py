# Task 1.3
# Create a program that asks the user for a number and then prints out a list of all the [divisors] /
# (https://en.wikipedia.org/wiki/Divisor) of that number.

def task_1_3_1(n):
    my_list = []
    for i in range(1, (int(n) + 1)):
        if int(n) % i == 0:
            my_list.append(i)
    print(my_list)