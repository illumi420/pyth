# Right Justify
"""
string = input("string: ")


def right_justify(s):
    length = len(s)
    if length <= 5:
        print(" " * 70, s)


right_justify(string) 
"""

#Exercise 3.4.
"""
def do_twice(f, g, value):
    for i in range(0, value, 1):
        f(g)
        f(g)


def print_spam():
    print("spam")


def print_twice(s):
    print(s)
    print(s)


#do_twice(print_twice, "spam", 2)


def do_four(f, g, value):
    for i in range(0, value, 1):
        f(g)


do_four(print_twice, "spam", 4)
"""
