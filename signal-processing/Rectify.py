import numpy as np
import matplotlib.pyplot as plt

# Load EMG data from the text file
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
emg_values = np.array(emg_values)

# Perform full-wave rectification
emg_rectified = np.abs(emg_values)

# Plot the original and rectified EMG signals
plt.figure(figsize=(10, 5))
plt.plot(time, emg_values, label='Original EMG')
plt.plot(time, emg_rectified, label='Rectified EMG')
plt.xlabel('Time')
plt.ylabel('EMG Value')
plt.title('Comparison of Original and Rectified EMG')
plt.legend()

# Save the plot
plt.savefig('fig4.png')