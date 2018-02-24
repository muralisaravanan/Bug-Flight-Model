import numpy as np
import matplotlib.pyplot as plt
import math




def euler (f,t_final,step, theta, alpha):
    time=[]
    height=[]
    t,z=0,0
    while t<=t_final:
        t+=step
        z+=step*f(t,z,theta,alpha)
        time.append(t)
        height.append(z)
    return time, height
        
def bug_flight(t,z,theta,alpha):
    first=-((2*alpha)/(1+2*alpha))*np.cos(np.sin(2*np.pi*t))*np.cos(2*np.pi*t)*2*np.pi
    second=-t
    third=-((2)/(1+2*alpha))*z
    fourth=-((2)/(1+2*alpha))*np.sin(np.sin(2*np.pi*t))
    fifth=(4*np.pi*alpha)/(1+2*alpha)
    return first+second+third+fourth+fifth

alpha1_time, alpha1_height=euler(bug_flight, 20, 0.1, 5, 0)
alpha2_time, alpha2_height=euler(bug_flight, 20, 0.1, 5, 0.1)
alpha3_time, alpha3_height=euler(bug_flight, 20, 0.1, 5, 1)
alpha4_time, alpha4_height=euler(bug_flight, 20, 0.1, 5, 10)
plt.figure(1)
plt.subplot(111)
plt.plot(alpha1_time, alpha1_height, 'k',alpha2_time, alpha2_height, 'k',alpha3_time, alpha3_height, 'k',alpha4_time, alpha4_height, 'k')
plt.ylabel("ggg")
plt.show()