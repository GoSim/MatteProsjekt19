import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

R = 10 #ohm

L = 5 * 10**(-3) #Henry

C = 50 * 10**(-6) #Farad

omega_0 = np.sqrt(1/(L*C)) 
zeta = R/(2*L*omega_0)
frekvens = 10000

#t, y = sig.step(system)


"""
plt.plot(t, y)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Step response for 1. Order Lowpass')

plt.grid()
plt.show()

"""



omega_1 = 1000
omega_2 = 2000
omega_3 = 4000
omega_4 = 8000

omega = omega_4

t = np.linspace(0, 0.02, 501) # Tidsvindu for simulering
v_0 = np.sin(omega*t)       # Påtrykt spenning v_inn(t)

numerator = [omega_0**2] #s + noe 
denominator = [1, 2*zeta*omega_0, omega_0**2]
system = sig.TransferFunction(numerator, denominator)
_, v_c, _ = sig.lsim(system, U=v_0, T=t)   # Beregn utgangsspenningen 'v_ut' gitt påtrykt spenning 'v_inn' for kretsen representert med 'system'

plt.plot(t, v_0, color="blue", label="v_0")
plt.plot(t, v_c, color="red", label="v_c")
plt.legend(loc="upper left")
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Spenning over v0 og Vc')

plt.text(0.015, 0.1, f"Frequency: {omega} Hz", transform=plt.gca().transAxes, fontsize=10, verticalalignment='bottom', bbox=dict(facecolor='white', alpha=0.5))


#plt.xlim(0.0062, 0.0194)

plt.grid()
plt.show()