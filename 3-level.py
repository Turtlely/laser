'''
2-level laser simulation

Assumptions:
1. Lasing medium is a homogenous and uniform spherical mass
2. No photons are lost
3. 100% of atoms begin initially in the 2nd excited state, after the initial pump

Units:
1 energy unit is equal to E2 - E1

Energy levels:
E1 = 0
E2 = 1
E3 = 2
'''

# Imports
import numpy as np
import matplotlib.pyplot as plt

# Lasing medium parameters
N = 100 # Number of atoms
E3 = 2 # Energy of 3rd level, relative to energy of 2nd level

# Laser Einstein Coefficient parameters
A12 = 1 # Spontaneous Emission
B21 = 1 # Stimulated Emission
B31 = 50 # Stimulated Emission from E3->E1

# Laser Non-radiative decay parameters
t_nr = 0.001 # Half life of non-radiative decay

# Photon parameters
Ep = 1 # Energy of a single photon

# Pump parameters
J_E = 200 # Energy delivered in a single pump (Units of E2-E1)
I0 = 1/100 # Intensity of a single pumped photon
T = 1000 # Pumping frequency

# Simulation parameters
t = 0
step = 0
dt = 0.001
tf = 20

# Initial Conditions
n1 = 100 # Number of atoms in the ground state
n2 = 0 # Number of atoms in the 1st excited state
n3 = 0 # Number of atoms in the 2nd excited state
E_pump = 0 # Amount of energy pumped into the system

# Logging
n1_t = [n1]
n2_t = [n2]
n3_t = [n3]
p_t = [0]
pi_t = [N/2]
t_t = [t]
r_t = [n2/n1*100]

while t<tf:
	# Calculate P, the photon intensity
	P = I0 * (E_pump - E3*n3 - Ep*n2)/Ep

	'''
	P_pump = 0
	
	# Pump the system at the beginning of simulation cycle, every T units of time
	if step%int(T/dt) == 0:
		E_pump += J_E # Add an additional J_E units of energy
		n1old = n1
		n3old = n3
		n1 = n3old
		n3 = n1old
	'''

	# Calculate n1' and n2'
	dn1_dt = A12*n2 + B21*P*(n2-n1) + B31*0.1*(n3-n1)
	dn2_dt = -1*B21*P*(n2-n1) - A12*n2 + np.log(2)/t_nr * n3
	dn3_dt = -1*np.log(2)/t_nr * n3 - B31*0.1*(n3-n1)



	# Calculate dn1 and dn2
	dn1 = dn1_dt * dt
	dn2 = dn2_dt * dt
	dn3 = dn3_dt * dt

	# Update n1 and n2
	n1 += dn1
	n2 += dn2
	n3 += dn3

	E_pump += 0.1

	# Timestep update
	t += dt
	step += 1

	# Logging
	n1_t.append(n1)
	n2_t.append(n2)
	n3_t.append(n3)
	p_t.append(P)
	pi_t.append(N/2)
	r_t.append(n2/n1*100)
	t_t.append(t)

plt.figure(1)
plt.title('3-Level laser population dynamics | Continuous Pumping \n' r'$A_{12}=$' f'{A12}, ' r'$B_{21}=$' f'{B21}, ' r'$\tau_{nr}=$' f'{t_nr}')
plt.plot(t_t, n1_t, label=r"$n_1$", c='blue')
plt.plot(t_t, n2_t, label=r"$n_2$", c='orange')
plt.plot(t_t, n3_t, label=r"$n_3$", c='red')
#plt.plot(t_t, pi_t, label="Population Inversion Threshold", linestyle="--", c='black')
plt.xlabel("Time")
plt.ylabel("N atoms")
plt.legend()

plt.figure(2)
plt.title('Population Inversion vs Time')
plt.plot(t_t, r_t, label=r"$n_2/n_1$", c='blue')
plt.plot(t_t, 2*np.array(pi_t), label="Population Inversion Threshold", linestyle="--", c='black')
plt.xlabel("Time")
plt.ylabel("%")
plt.ylim(0,200)
plt.legend()


plt.show()
