import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt

R = 10 #ohm

L = 5 * 10**(-3) #Henry

C = 50 * 10**(-6) #Farad

omega_0 = np.sqrt(1/(L*C)) 
zeta = R/(2*L*omega_0)

print(omega_0)

print(zeta)



numerator = [omega_0**2] #s + noe 
denominator = [1, 2*zeta*omega_0, omega_0**2]
system = sig.TransferFunction(numerator, denominator)

t, y = sig.step(system)

plt.plot(t, y)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Step response for 1. Order Lowpass')

print(zeta)
plt.grid()
plt.show()