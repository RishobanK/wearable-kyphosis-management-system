import numpy as np
import matplotlib.pyplot as plt

# Read EMG data from file
file_name = 'EMG.txt'
time = []
emg_values = []

with open(file_name, 'r') as file:
    for line in file:
        if line.strip():  # Check if the line is not empty
            emg, t = line.strip().split(', ')
            emg_values.append(float(emg))
            time.append(float(t))

# Convert lists to numpy arrays for easier manipulation
time = np.array(time)
emg_values = np.array(emg_values)

# Plot EMG signal
plt.figure(figsize=(12, 6))
plt.plot(time, emg_values, label='EMG Signal')
plt.xlabel('Time (s)')
plt.ylabel('EMG Signal (a.u.)')
plt.title('EMG Signal Over Time')
plt.legend()
plt.grid(True)

# Save the plot as an image
plt.savefig('emg_plot.png')