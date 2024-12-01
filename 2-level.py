'''
2-level laser simulation

Assumptions:
1. Lasing medium is a homogenous and uniform spherical mass
2. No photons are lost
3. 100% atoms begin initially in the ground state, prior to the initial pump
'''

# Imports
import numpy as np
import matplotlib.pyplot as plt

# Lasing medium parameters
N = 100 # Number of atoms

# Laser Einstein Coefficient parameters
A12 = 1 # Spontaneous Emission
B21 = 1 # Stimulated Emission

# Photon parameters
Ep = 1 # Energy of a single photon

# Pump parameters
J_E = 100 # Energy delivered in a single pump (Units of # of atoms)
I0 = 1/100 #Intensity of a single photon
T = 10 # Pump the system every T units of time


# Simulation parameters
t = 0
step = 0
dt = 0.01
tf = 30

# Initial Conditions
n1 = 100 # Number of atoms in the ground state
n2 = N-n1 # Number of atoms in the excited state
E_pump = 0 # Amount of energy pumped into the system via optical pumps

# Logging
n1_t = [n1]
n2_t = [n2]
pi_t = [N/2]
t_t = [t]

while t<tf:
	# Calculate P, the photon intensity
	#P = I0 * (1 - (Ep*n2/J_E))
	
	# Pump the system at the beginning of simulation cycle, every T units of time
	if step%int(T/dt) == 0:
		E_pump += J_E # Add an additional J_E units of energy

	# Calculate P, the photon intensity
	P = I0*(E_pump - Ep*n2)/Ep

	# Calculate n1' and n2'
	dn1_dt = A12*n2 + B21*P*(n2-n1)
	dn2_dt = -1*B21*P*(n2-n1) - A12*n2
	#dn1_dt = A12*n2 + B21*Np*(n2-n1)
	#dn2_dt = -1*B21*Np*(n2-n1) - A12*n2

	# Calculate dn1 and dn2
	dn1 = dn1_dt * dt
	dn2 = dn2_dt * dt

	# Update n1 and n2
	n1 += dn1
	n2 += dn2

	# Timestep update
	t += dt
	step += 1

	# Logging
	n1_t.append(n1)
	n2_t.append(n2)
	pi_t.append(N/2)
	t_t.append(t)

plt.figure(1)
plt.title('2-Level laser population dynamics\n' r'$A_{12}=$' f'{A12}, ' r'$B_{21}=$' f'{B21}')
plt.plot(t_t, n1_t, label=r"$n_1$", c='blue')
plt.plot(t_t, n2_t, label=r"$n_2$", c='red')
plt.plot(t_t, pi_t, label="Population Inversion Threshold", linestyle="--", c='black')
plt.ylim(0,100)
plt.legend()
plt.xlabel("Time")
plt.ylabel("N atoms")
plt.show()
