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

