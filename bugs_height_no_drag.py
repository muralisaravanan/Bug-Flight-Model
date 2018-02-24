import numpy as np
import matplotlib.pyplot as plt
import math

def f(t,alpha):
    first=-(1/2)*t**2
    second= ((4*alpha*np.pi)/(1+2*alpha))*t
    third=-((2*alpha)/(1+2*alpha))*np.sin(np.sin(2*np.pi*t))
    return first +second+third

t1 = np.arange(0.0, 13.0, 0.02)
t2 = np.arange(0.0, 13.0, 0.02)

plt.figure(1)
plt.subplot(111)
plt.plot(t1, f(t1, 0), 'k', t1, f(t1, 0.1), 'k', t1, f(t1, 1), 'k', t1, f(t1, 10), 'k')
plt.ylabel("ggg")
plt.show()