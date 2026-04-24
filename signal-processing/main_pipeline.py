import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def process_emg(time, emg_signal):
    # Example function to process EMG signal
    emg_mean_removed = remove_mean(emg_signal)
    emg_filtered = filter_emg(emg_mean_removed)
    emg_rectified = rectify_emg(emg_filtered)
    return emg_mean_removed, emg_filtered, emg_rectified

def remove_mean(emg_signal):
    return emg_signal - np.mean(emg_signal)

def filter_emg(emg_signal):
    # Example bandpass filter parameters
    fs = 1000  # Sampling frequency (Hz)
    lowcut = 20  # Low cutoff frequency (Hz)
    highcut = 450  # High cutoff frequency (Hz)
    order = 4  # Filter order

    b, a = signal.butter(order, [lowcut / (fs / 2), highcut / (fs / 2)], btype='band')
    
    # Check if signal length is sufficient for filtering
    if len(emg_signal) <= 27:
        raise ValueError("The length of the EMG signal must be greater than 27 samples for filtering.")
    
    emg_filtered = signal.filtfilt(b, a, emg_signal)
    return emg_filtered

def rectify_emg(emg_signal):
    return np.abs(emg_signal)

def main(filename):
    # Example main function to process EMG data
    time, emg = read_emg(filename)
    emg_mean_removed, emg_filtered, emg_rectified = process_emg(time, emg)
    plot_results(time, emg, emg_mean_removed, emg_filtered, emg_rectified)

def read_emg(filename):
    # Example function to read EMG data from file
    time = []
    emg_values = []
    
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():  # Check if the line is not empty
                try:
                    emg, t = map(float, line.strip().split(', '))
                    emg_values.append(emg)
                    time.append(t)
                except ValueError:
                    print(f"Skipping line due to conversion error: {line.strip()}")
    
    time = np.array(time)
    emg_values = np.array(emg_values)
    return time, emg_values

def plot_results(time, emg, emg_mean_removed, emg_filtered, emg_rectified):
    # Example function to plot EMG data
    plt.figure(figsize=(12, 8))
    
    plt.subplot(3, 1, 1)
    plt.plot(time, emg, label='Original EMG')
    plt.xlabel('Time')
    plt.ylabel('EMG Value')
    plt.title('Original EMG')
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(time, emg_mean_removed, label='Mean Removed EMG')
    plt.xlabel('Time')
    plt.ylabel('EMG Value')
    plt.title('Mean Removed EMG')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(time, emg_filtered, label='Filtered and Rectified EMG')
    plt.xlabel('Time')
    plt.ylabel('EMG Value')
    plt.title('Filtered and Rectified EMG')
    plt.legend()

    plt.tight_layout()

    # Save the plot
    plt.savefig('Processed signal.png')

if __name__ == "__main__":
    filename = 'EMG.txt'
    main(filename)
