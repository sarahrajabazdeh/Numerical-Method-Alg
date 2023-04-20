import numpy as np
import matplotlib.pyplot as plt
from Numeric import *
import sys
import math

x_value = [] 
t_value = []
global x, t0
x = 0.5
t0 = 0.0

def f(k,y):
	return y*(1.0-y)
	
def calculate_rungekutta_param(x0,t0,h):
	k1 = h*f(t0,x0)
	k2 = h*f(t0 + h/2, x0 + k1/2)
	k3 = h*f(t0 + h/2, x0 + k2/2)
	k4 = h*f(t0 + h, x0 + k3)
	
	k = (1.0/6.0)*(k1 + 2*k2 + 2*k3 + k4)
	
	return k

def plot_diagram():
	global x
	t = 0.0
	h = 0.1
	for value in arange(0.1,5.0,0.1):
		l = calculate_rungekutta_param(x,t,h)
		x = x + l
		x_value.append(x)
		t = t + h
		t_value.append(t)
		
	
	t = np.arange(0.0, 5.0, 0.1)
	x_derivatives = np.arange(-15.0, 30.0, 1.0)
	plt.figure(1)
	plt.subplot(111)
	plt.xlabel('time (t) ')
	plt.ylabel('displacement (x) ')
	plt.title('Graph Between X and t')
	plt.plot(t_value,x_value)
	
	plt.figure(2)
	plt.subplot(211)
	plt.xlabel('value of x (x)')
	plt.ylabel('value of x_das (y) ')
	plt.title('Graph Between X derivatives and x')
	plt.plot(x_derivatives,f(t0,x_derivatives))
	plt.axis([-25.0, 25.0,-600.0,0.0])
	plt.show()

if __name__ == "__main__":
	plot_diagram()