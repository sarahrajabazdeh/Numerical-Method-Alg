import math
def samesign(a, b):
    return a * b > 0

def bisect(func, low, high, tolerance=None):
    assert not samesign(func(low), func(high))   
    for i in range(54):
        midpoint = (low + high) / 2.0
        if samesign(func(low), func(midpoint)):
            low = midpoint
        else:
            high = midpoint
        if tolerance is not None and abs(high - low) < tolerance:
            break   
    return midpoint
    
def f(x):
        return math.exp(x) + math.cos(x)-2   
x = bisect(f, 0, 1)
print(x, f(x))        