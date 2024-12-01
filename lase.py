import matplotlib.pyplot as plt
import numpy as np

def rectangular_pulse(t_cycle, A, t):
    """
    Generates a rectangular pulse function that turns on cyclically every t_cycle seconds,
    and lasts A seconds.
    
    Parameters:
    t_cycle : float
        The cycle time in seconds (time period for the pulse to turn on and off).
    A : float
        The duration for which the pulse is on (in seconds).
    t : numpy array
        Array of time points where the function should be evaluated.
    
    Returns:
    numpy array : Pulse values (1 if on, 0 if off).
    """
    return np.where((np.mod(t, t_cycle) < A), 1, 0)

# Number of atoms in the bulk simulation
n0=100 # Ground state
n1=0 # Lower lasing state
n2=0 # Higher lasing state

# Photon parameters
n_coherent = 0
n_incoherent = 60
I0 = 0.001 # Intensity of a single photon

# Pump parameters
I_max = 10 # Intensity of optical pump

# Simulation parameters
t = 0
dt = 0.001
tf = 60
nsteps = int((tf-t)/dt)

# Kinetics
y_sp = 1 # E2->E1 spontaneous decay
y_nr = 0 # E2->E1 nonradiative decay
y_10 = 0.5 # E1->E0 spontaneous decay
B_10 = 1 # E1->E0 stimulated emission
s_abs = 8.25 # E0->E1 absorption
s_pump = 1 # E0->E3 absorption

# Logging
n0_t = [n0]
n1_t = [n1]
n2_t = [n2]
t_t = [t]

for _ in range(nsteps):
	I_pump = I_max*rectangular_pulse(100, 0.1, t)
	dn2dt = s_pump*I_pump*n0 - (y_sp + y_nr)*n2
	dn1dt = (y_sp + y_nr)*n2 + s_abs*I0*(n_coherent+n_incoherent)*n0 - (y_10 + B_10*I0*(n_coherent+n_incoherent))*n1
	dn0dt = (y_10 + B_10*I0*(n_coherent+n_incoherent))*n1 - s_abs*I0*(n_coherent+n_incoherent)*n0 - s_pump*I_pump*n0
	#dicdt = y_10*n1
	dcdt = B_10*I0*(n_coherent+n_incoherent)*n1


	n0 += dn0dt*dt
	n1 += dn1dt*dt
	n2 += dn2dt*dt
	#n_incoherent += dicdt*dt
	n_coherent += dcdt*dt

	t += dt

	# Logging
	n0_t.append(n0)
	n1_t.append(n1)
	n2_t.append(n2)
	t_t.append(t)

plt.plot(t_t,n0_t,label="E0")
plt.plot(t_t,n1_t,label="E1")
plt.plot(t_t,n2_t,label="E2")
plt.legend()
plt.show()