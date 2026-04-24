import numpy as np
import matplotlib.pyplot as plt

# Read EMG data from file
file_name = 'EMG.txt'
time = []
emg_values = []

with open(file_name, 'r') as file:
    for line in file:
        if line.strip():  # Check if the line is not empty
            try:
                emg, t = line.strip().split(', ')
                emg_values.append(float(emg))
                time.append(float(t))
            except ValueError:
                print(f"Skipping line due to conversion error: {line.strip()}")

# Convert lists to NumPy arrays
time = np.array(time)
emg = np.array(emg_values)

# Process EMG signal: remove mean
emg_correctmean = emg - np.mean(emg)

# Plot comparison of EMG with offset vs mean-corrected values
fig = plt.figure()

plt.subplot(1, 2, 1)
plt.title('Mean offset present')
plt.plot(time, emg)
plt.locator_params(axis='x', nbins=4)
plt.locator_params(axis='y', nbins=4)
plt.ylim(-80, 80)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')

plt.subplot(1, 2, 2)
plt.title('Mean-corrected values')
plt.plot(time, emg_correctmean)
plt.locator_params(axis='x', nbins=4)
plt.locator_params(axis='y', nbins=4)
plt.ylim(-100, 100)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')

fig.tight_layout()
fig_name = 'fig2.png'
fig.set_size_inches(w=11, h=7)
fig.savefig(fig_name)

# Save the plot as an image
plt.savefig('fig2.png')
