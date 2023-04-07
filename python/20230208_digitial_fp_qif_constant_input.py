from pylab import *
import matplotlib.pyplot as plt
import numpy as np
def u(t):
    return .5*(sign(t)+1)
 

b=.1                        #Set the parameter b.
Vpeak = 1                     #Define the voltage threshold.
Vreset = -1                 #Define the reset voltage.
dt=0.004                    #Set the timestep.
V = zeros([10000,1])        #Initialize V.
V[0]=-0                     #Set the initial condition.
a=1                         #Set the gain of the multiplier condition.

for k in range(1,len(V)-1):       #March forward in time,
    V[k+1] = V[k]+a*dt*V[k]**2+ dt*b #Update the voltage,
    if V[k+1] > Vpeak:         #... and check if the voltage exceeds the threshold.
        V[k+1] = Vreset
        
t = arange(0,len(V))*dt      #Define the time axis.


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
fig.subplots_adjust(left=0.25, bottom=0.25)
legend='$b={},V_{{reset}}={},V_{{peak}}={},a={},dt={}$'.format(b,Vreset,Vpeak,a,dt)
[line] = ax.plot(t, V, linewidth=2, color='blue',label=legend)
ax.set_xlabel('Time (s)',fontsize=12)
ax.set_ylabel('Arbritrary units',fontsize=12) 
ax.legend()
plt.title('Digital (Floating Point) QIF transient response to a constant input')
ax.grid()
plt.show()
 
 