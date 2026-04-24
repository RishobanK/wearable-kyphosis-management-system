import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Load EMG data from the text file
with open('EMG.txt', 'r') as file:
    lines = file.readlines()

# Extract EMG values from the loaded data
emg_values = []
for line in lines:
    if line.strip():  # Check if the line is not empty
        try:
            emg, _ = map(float, line.strip().split(','))
            emg_values.append(emg)
        except ValueError:
            print(f"Skipping line due to conversion error: {line.strip()}")

# Convert the list of EMG values to a NumPy array
emg_values = np.array(emg_values)

# Ensure there are enough data points for the filter
if len(emg_values) <= 27:
    raise ValueError("The length of the EMG data must be greater than 27 samples for filtering.")

# Create a bandpass filter for the EMG signal
fs = 1000  # Sampling frequency (Hz)
low_cut = 20  # Low cut-off frequency (Hz)
high_cut = 450  # High cut-off frequency (Hz)
order = 4  # Filter order

b, a = signal.butter(order, [low_cut / (fs / 2), high_cut / (fs / 2)], btype='band')

# Apply the bandpass filter to the EMG signal
emg_filtered = signal.filtfilt(b, a, emg_values)

# Plot the original and filtered EMG signals
plt.figure(figsize=(10, 5))
plt.plot(emg_values, label='Original EMG')
plt.plot(emg_filtered, label='Filtered EMG')
plt.xlabel('Time')
plt.ylabel('EMG Value')
plt.title('Comparison of Original and Filtered EMG')
plt.legend()

# Save the plot
plt.savefig('fig3.png')
