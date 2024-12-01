import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Initialize parameters
N = 400
h = 5
w = 10
photons = []
atoms = []

r_abs = 1
y_abs = 5
y_10 = 5
y_sp = 10
y_nr = 10
B_10 = 20

# Add a photon at x, y moving in a random direction
def addPhoton(x, y, theta=None):
    if theta==None:
        theta = 2 * np.pi * np.random.rand()
    photons.append([[x, y], theta])

def addAtom(x, y, E):
    atoms.append([[x, y], E])

for n in range(N):
    addAtom(w * (np.random.rand() - 0.5), h * (np.random.rand() - 0.5), 2)

# Simulation parameters
t = 0
dt = 0.01
t_f = 100
c = 10  # Speed of light

# Add an initial photon
addPhoton(0, 0)

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(-w / 2 - 1, w / 2 + 1)
ax.set_ylim(-h / 2 - 1, h / 2 + 1)
scat = ax.scatter([], [], s=10, c='red')  # Photons scatter
atom_scat = ax.scatter([], [], s=20, c='green')  # Atoms scatter

# Draw the rectangle
rectangle = patches.Rectangle(
    (-w / 2, -h / 2), w, h, linewidth=1, edgecolor='blue', facecolor='none'
)
ax.add_patch(rectangle)

# Update function for animation
def update(frame):
    global photons, atoms, t
    t += dt
    new_photon_positions = []

    for atom in atoms:
        x, y = atom[0]
        E = atom[1]

        if E == 0:
            # Absorb a photon or get excited by pump
            absorbed_photon = None
            # Search list of photons for any within distance r_abs
            for photon in photons:
                px, py = photon[0]
                # Calculate the distance between the photon and atom
                distance = np.sqrt((x - px)**2 + (y - py)**2)
                if distance < r_abs:
                    if np.random.rand() < y_abs * dt:  # Absorb with rate constant y_abs
                        absorbed_photon = photon
                        atom[1] = 1  # Excite atom to E=1
                        print("Absorbed")
                        break  # Absorb only one photon per time step
            # Remove absorbed photon from list
            if absorbed_photon is not None:
                photons.remove(absorbed_photon)

        elif E == 1:
            # Emit a photon (spontaneous emission)
            if np.random.rand() < y_10 * dt:  # Probability of spontaneous emission
                addPhoton(x, y)  # Emit photon
                atom[1] = 0  # Decay to E=0
                print("Spontaneous Decay")

            # Stimulated emission: Generate a new photon in the same direction as the incident photon
            # Search list of photons for any within distance r_abs
            for photon in photons:
                px, py = photon[0]
                # Calculate the distance between the photon and atom
                distance = np.sqrt((x - px)**2 + (y - py)**2)
                if distance < r_abs:
                    if np.random.rand() < B_10 * dt:  # Stimulated emission with rate constant B_10
                        # Generate a new photon in the same direction as the incident photon
                        photon_theta = photon[1]
                        addPhoton(x, y, theta=photon_theta)  # New photon created at atom's position with same direction
                        atom[1] = 0  # Atom decays from E=1 to E=0
                        print("Stimulated Emission")
                        break  # Only one photon per time step

        elif E == 2:
            # Decay to E=1
            if np.random.rand() < (y_sp + y_nr) * dt:  # Probability of decay
                atom[1] = 1  # Decay to E=1

    # Update photons
    for photon in photons:
        x, y = photon[0]
        theta = photon[1]

        if -h / 2 < y < h / 2:  # Photon inside height bounds
            # Update position
            vx = c * np.sin(theta)
            vy = c * np.cos(theta)
            if -w / 2 < x + vx * dt < w / 2:  # Photon inside width bounds
                photon[1] *= 1
            else:
                photon[1] *= -1  # Reverse direction upon hitting width bounds

            photon[0] = [x + vx * dt, y + vy * dt]
            new_photon_positions.append(photon)

    photons = new_photon_positions

    # Update scatter plot data for photons
    photon_positions = [photon[0] for photon in photons]
    if photon_positions:
        scat.set_offsets(photon_positions)
    else:
        scat.set_offsets([])

    # Update scatter plot data for atoms
    atom_positions = [atom[0] for atom in atoms]
    atom_colors = ['blue' if atom[1] == 0 else 'orange' if atom[1] == 1 else 'purple' for atom in atoms]
    atom_scat.set_offsets(atom_positions)
    atom_scat.set_color(atom_colors)

# Create animation
ani = FuncAnimation(fig, update, frames=int(t_f / dt), interval=dt * 1000, repeat=False)

plt.show()
