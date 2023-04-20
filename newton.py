import matplotlib.pyplot as plt
import numpy as np
import math

def f(x):
    return math.exp(x) + math.cos(x)-2   

def derivative(f, x):
    return math.exp(x) - math.sin(x)

def x_next(f, x_n):
    return x_n - (f(x_n) / derivative(f, x_n))

iterations = []
error = []
def newtons_method(f, x_n = 1, i = 0, max_iter = 100):
    i = i + 1
    if (i == max_iter):
        return None
    x_n = x_next(f, x_n)
    print("i:",i,"x_n:",x_n,"f(x_n)",f(x_n))
    error.append(abs(f(x_n)))
    iterations.append(i)
    if (abs(f(x_n)) < 1E-12):
        return x_n
    newtons_method(f, x_n, i, max_iter)

newtons_method(f)
plt.semilogy(iterations, error, label = "error plot")
plt.show()

