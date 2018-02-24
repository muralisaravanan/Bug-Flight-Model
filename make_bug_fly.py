import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal



def theta(t):
    return -signal.sawtooth(2 * np.pi *200* t)
def dtheta(t):
    return -200

def euler (f,t_final,step,alpha):
    time=[]
    height=[]
    t,z=0,0
    while t<=t_final:
        t+=step
        z+=step*f(t,z,theta,dtheta,alpha)
        time.append(t)
        height.append(z)
    return time, height
        
def bug_flight(t,z,theta,dtheta,alpha):
    first=-((2*alpha)/(1+2*alpha))*np.cos(theta(t))*dtheta(t)
    second=-t
    third=-((2)/(1+2*alpha))*z
    fourth=-((2)/(1+2*alpha))*theta(t)
    fifth=(4*np.pi*alpha)/(1+2*alpha)
    return first+second+third+fourth+fifth



#theta=np.sin(2*np.pi*t)
#dtheta=np.cos(2*np.pi*t)*2*np.pi

alpha1_time, alpha1_height=euler(bug_flight, 100, 1e-4, 0)
alpha2_time, alpha2_height=euler(bug_flight, 100, 1e-4, 0.1)
alpha3_time, alpha3_height=euler(bug_flight, 100, 1e-4, 1)
alpha4_time, alpha4_height=euler(bug_flight, 100, 1e-4, 10)

plt.figure(2)
plt.subplot(211)
plt.plot(alpha1_time, alpha1_height, 'k',alpha2_time, alpha2_height, 'k',alpha3_time, alpha3_height, 'k',alpha4_time, alpha4_height, 'k')


theta_val=[]
for t in alpha1_time:
    theta_val.append(theta(t))
plt.subplot(212)
plt.plot(alpha1_time,theta_val, 'k')
plt.show()