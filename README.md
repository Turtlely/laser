# Laser Physics
The purpose of this repository is to teach myself some basic concepts in laser physics.

I found this project very fun, I hope you do too!

# What are lasers

The objective of a laser is to produce a beam of coherent photons of a single wavelength. Essentially, we want to input some amount of energy, and convert as much of that energy into coherent photons as possible.

In practice, this is done via "pumping". Pumping is the process of adding energy to the laser system, often via optical methods.

The first laser, a ruby laser, utilized an optical pump. This optical pump was a flash lamp that rapidly released a flash of bright light, which was quickly absorbed by the lasing medium, a ruby crystal. After absorbing the energy, the ruby crystal would release a flash of coherent photons known as the laser beam.

Lasers typically have colimated beams, which is achieved via an optical resonator. Two mirrors are placed at either end of the optical cavity and reflect light back and forth to filter only for photons travelling in the same direction.

![alt](https://upload.wikimedia.org/wikipedia/commons/9/92/Lasercons.svg)

# Laser Dynamics / Kinetics

A laser fundamentally operates off the principle that photons are emitted or absorbed upon the demotion or promotion of an electron from an energy level respectively.

A two-level laser has two energy levels, which we can denote as $E_1$ and $E_2$, with $E_2$ > $E_1$.
- We denote the energy difference $E_2 - E_1$ as $\Delta{E}$.

Within a two-level laser, there are three main processes at play:
1. Spontaneous Emission
   - The spontanous emission of a photon due to the decay of an electron from $E_1$ to $E_2$. The emitted photon has a random direction and phase, and is said to be "incoherent."
3. Stimulated Emission
   - An electron is "stimulated" to decay, due to the effects of another photon passing by. The emitted photon has identical phase and direction as the "stimulating" photon.
5. Absorption
   - An electron is promoted to a higher energy level by the absorption of a photon of the right energy.

Each of these processes follows a certain set of kinetic equations.

![alt](https://blogger.googleusercontent.com/img/a/AVvXsEgEJYr2uUS1HtY42fWg1Qo0RN8jkKlMYGdCW96LSdDhD4HAc5KReA6IH6EvwuF3FapMxONthBdwzfidpjJyVqDK-dL_Bb8Q1PsUa7hcJCZcOGh4BvJg3Wdh3aibji1IYmeROmE8jx6fPfVxaMYPf_UgkfVWl5vNzc7BJ95D60iVLDikKuT475iT0s9L=w1200-h630-p-k-no-nu)

## Spontaneous Emission
Suppose we have a population of N_2 atoms in the $E_2$ state. The rate at which this population will change due to spontaneous absorption is as follows:

$\frac{\partial{N_2}}{\partial{t}}=-A_{21}N_2$, where $A_21$ is called the "Einstein A Coefficient" for the $E_2$ --> $E_1$ transition. It acts as a sort of rate constant.

## Stimulated Emission
Supposing again we have a population of $N_2$ $E_2$ atoms, the rate at which stimulated emission occurs is as follows:

$\frac{\partial{N_2}}{\partial{t}} = -B_{21}\rho(\nu)N_2$, where $\rho(\nu)$ is the incident intensity of photons capable of causing stimulated emission, and $B_21$ is called the "Einstein B coefficient" for the 2 --> 1 transition.

## Absorption
If we have a population of N_1 $E_1$ atoms, the rate at which absorption occurs is as follows:
$\frac{\partial{N_1}}{\partial{t}} = -B_{21}\rho(\nu)N_1$, where $\rho(\nu)$ is the incident intensity of photons capable of being absorbed, and $B_12$ is called the "Einstein B coefficient" for the 1 --> 2 transition.

Because we know that the only two states for atoms are either $E_1$ or $E_2$, we know that $\frac{\partial{N_1}}{\partial{t}} = -\frac{\partial{N_2}}{\partial{t}}$

Einstein also showed that $B_{21} = B_{12}$, essentially meaning that stimulated emission and absorption are reverse processes that occur at different rates.

From these individual rate laws, we finally get the following differential equation:

```math
\frac{\partial{N_2}}{\partial{t}} = B_{21}\rho(\nu)(N_2-N_1) - A_{12}N_1
```

## The value of $\rho(\nu)$
$\rho(\nu)$ represents the radiant energy density of photons of the wavelength $\nu$, capable of causing stimulated emission or absorption.
This can be found by considering conservation of energy.

Lets say that we initially start out with a population of $N_2$ atoms in state $E_2$. Over time, we find that the system now contains $N_1$ atoms in state $E_1$, where $N_1 = N_2$.
This means that all atoms that were originally in state $E_2$ have been converted to state $E_1$, releasing $\Delta{E}$ energy per atom. This released energy must be in the form of photons if we assume no thermal losses.
Therefore, each photon released has energy $\Delta{E}=h\nu$. If the lasing medium has volume $V$, then:

```math
\rho(\nu) = \frac{N_1\Delta{E}}{V}
```

Assuming of course, that all atoms were intially in the $E_2$ state initially.

# Simulating a 2-level laser

All together, we can now solve these differential equations to see the population dynamics of a 2-level laser over time.
![alt](https://github.com/Turtlely/laser/blob/0909f7915b4798add16ce9d0506646c217401829/2-level.png)

Here, we pump the system initially, providing enough energy to convert some atoms from $E_1$ into $E_2$. As a result, $N_1$ drops and $N_2$ increases. We then periodically continue to pump this system to add more energy in.

However, you might notice that we never achieve $N_2 > N_1$. This condition is called population inversion, and is necessary for a self-sustaining lasing state, where coherent photons are allowed to build up in the system.

Sustained population inversion is a necessary condition to achieve lasing, as it means that there is a >50% chance that a photon will encounter an excited atom to cause stimulated emission and thus amplify the original signal.

Without population inversion, the system will have a net absorption of photons at any time, meaning that a population of coherent photons is not able to build up and create the laser beam.

# 3-level lasers

It is impossible to efficiently achieve a sustained state of population inversion in a 2-level laser when using optical pumping. However, if we add a new energy level to the system, we can achieve sustained population inversion.
Lets create a new energy level, $E_3$, which is the highest in energy.

We will utilize optical pumping to excite atoms from $E_1$ to $E_3$, and then allow $E_3$ to quickly decay to $E_2$ in a non-radiative process. Then, we allow $E_2$ to decay to $E_1$ slowly, releasing our desired laser light.

![alt](https://upload.wikimedia.org/wikipedia/commons/4/41/Population-inversion-3level.png)

This system is able to achieve population inversion because we are able to continuously pump the system, filling the $E_3$ energy level. Atoms in $E_3$ then quickly trickle into the $E_2$ state.

Unlike with a two-level laser, 3-level lasers are able to achieve population inversion because the optical pumping does not remove atoms from our excited lasing state $E_2$. You have to remember that optical pumping can both cause atoms to be excited to a higher energy state, but also cause atoms to decay to a lower energy state via stimulated emission. In a 2-level laser, optical pumping will kill off the excited atom population, meaning that at best, a 50% population inversion can be achieved.

Lets take a look at a 3-level laser system.
![alt](https://github.com/Turtlely/laser/blob/0909f7915b4798add16ce9d0506646c217401829/3-level.png)

As you can see, in the steady state, we are able to achieve a >50% population inversion in this 3-level laser.

Lasing has been achieved!
