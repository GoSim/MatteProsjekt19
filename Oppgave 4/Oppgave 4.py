from scipy.io import wavfile
import scipy.signal as sig
from IPython.display import Audio
import matplotlib.pyplot as plt
import numpy as np

def main():
    

    fs, data = wavfile.read('RockDrums-48-mono-11secs.wav')
    #print(fs)
    #print(data.shape[0])
    #audioSignal = data*1.0
    audioSignal = data*1.0

    Audio(audioSignal, rate=fs)
    #print(audioSignal)

    time = np.linspace(0, (len(audioSignal)-1)/fs, len(audioSignal))
    plt.plot(time, audioSignal)
    plt.xlabel("Tid $t$ [s]")
    plt.ylabel("")

    #plt.show()
    
    R = 10
    L = 5*10**(-3)
    C = 50*10**(-6)

    omega_0 = np.sqrt(1/(L*C)) 
    zeta = R/(2*L*omega_0)
    
    num1 = [omega_0**2]
    den1 = [1, 2*zeta*omega_0, omega_0**2]
    tf1 = sig.TransferFunction(num1,den1)
    tout, yout, xout = sig.lsim(tf1,audioSignal,time)
    plt.plot(tout,yout)
    
    frequence = np.linspace(10e1, 10e5, 100000)
    omega1, mag1, phase1 = sig.bode(tf1, w=frequence)
    plt.figure(2)
    plt.xlabel("Frekvens [1/s]")
    plt.ylabel("Magnitude [dB]")
    plt.grid()
    plt.gca().set_xlim(10e1,10e4)
    #plt.gca().set_ylim(-55,5)
    plt.semilogx(omega1, mag1)     
    plt.figure(3)
    plt.xlabel("Frekvens [1/s]")
    plt.ylabel("Phase [deg]")
    plt.grid()
    plt.gca().set_xlim(10e1,10e4)
    plt.gca().set_ylim(-180,180)
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(90))
    plt.semilogx(omega1, phase1)
    #plt.show()
    
    wavfile.write("(LPF)RockDrums-48-mono-11secs.wav",fs,xout)
    

    ###### Oppgave b ############################################


    #num2 = [1,0,0]
    #den2 = den1
    num2 = [1,0,(L*C)**2]
    den2 = [0,0,1]

    tf2 = sig.TransferFunction(num2,den2)
    print(tf2)
    omega2, mag2, phase2 = sig.bode(tf2, w=frequence)

############################################
    plt.figure(2)
    plt.semilogx(omega2, mag2)
    plt.legend(["tf1", "tf2"], loc="lower right")   
    plt.figure(3)
    plt.semilogx(omega2, phase2)
    plt.legend(["tf1", "tf2"], loc="lower right") 
############################################    

    tout,yout, xout  = sig.lsim((num2,den2),audioSignal,time)
    plt.figure(1)
    plt.plot(tout,yout)
    plt.legend(["ufiltrert signal", "tf1", "tf2"], loc="lower right") 
    plt.show()
    
    wavfile.write("(HPF)RockDrums-48-mono-11secs.wav", fs, xout)
    return


if __name__ == "__main__":
    main()

