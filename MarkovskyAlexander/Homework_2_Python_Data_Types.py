# Task 1.1
# Write a Python program to calculate the length of a string without using the `len` function.

def task_1_1(n):
    count = 0
    for _ in str(n):
        count += 1
    print("Length of a string: ", count)


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


# Task 1.3
# Write a Python program that accepts a comma separated sequence of words as input and prints the unique /
# words in sorted form.

def task_1_3(*args):
    print(sorted(set(*args)))


# Task 1.3
# Create a program that asks the user for a number and then prints out a list of all the [divisors] /
# (https://en.wikipedia.org/wiki/Divisor) of that number.

def task_1_3_1(n):
    my_list = []
    for i in range(1, (int(n) + 1)):
        if int(n) % i == 0:
            my_list.append(i)
    print(my_list)


# Task 1.4
# Write a Python program to sort a dictionary by key.

def task_1_4(dictionary):
    for key in sorted(dictionary):
        print("%s: %s" % (key, dictionary[key]))


# Task 1.5
# Write a Python program to print all unique values of all dictionaries in a list.

def task_1_5(array):
    list_1 = []
    for i in array:
        for v in i:
            list_1.append(i.get(v))
    print(set(list_1))


# Task 1.6
# Write a Python program to convert a given tuple of positive integers into an integer.

def task_1_6(nums):
    result = int(''.join(map(str, nums)))
    return result


# Task 1.6
# Write a program which makes a pretty print of a part of the multiplication table.

def task_1_6_1(a, b, c, d):
    for j in range(c, d + 1):
        print("\t" + str(j), end="")
    print()
    for i in range(a, b + 1):
        print(i, end="\t")
        for k in range(c, d + 1):
            print(i * k, end="\t")
        print()


