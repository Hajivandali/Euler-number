"""
Solve Nepper number with functional programming
Language = python 3.9

Run the program:
    Power function
    Factorial function
    Nepper main function

** (math) Math import is laid out just for comparison with my code **
v = 1.0.0
"""


def square(n):
    r = n**2
    return r


def cube(n):
    return square(n)*n


def nepper(x=1, y=18):
    r = 0
    for i in range(y+1):
        r += pow_(x, i)/factorial(i)
    return r


def pow_(a, b):
    r = 1
    for i in range(b):  #2+2+2
        r = r*a
    return r


def factorial(n):
    r = 1
    for i in range(1, n+1):
        r = r*i
    return r


if __name__ == "__main__":
    import math
    print(math.e)
    print(nepper(1, 18))    #sample 1 , 18
