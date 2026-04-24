# Signal Processing

This module processes raw EMG (Electromyography) signals using Python.

---

## Overview

The scripts implement a basic EMG signal-processing pipeline to extract useful information from raw muscle activity data.

The processing is performed offline using recorded data.

---

## Processing Steps

1. Mean Removal  
2. Bandpass Filtering (20–450 Hz)  
3. Rectification  
4. Visualization  

---

## Files

- main_pipeline.py — Complete EMG processing pipeline  
- remove_mean.py — Mean removal  
- filter_emg.py — Bandpass filtering  
- rectify_emg.py — Signal rectification  
- plot_emg.py — Visualization  

---

## Input Format

The scripts expect EMG data in the following format:

```text
emg_value, time
```

Example:

```text
0.23, 0.001
0.45, 0.002
0.12, 0.003
```

---

## Requirements

- Python 3.x  
- numpy  
- scipy  
- matplotlib  

Install dependencies:

```bash
pip install numpy scipy matplotlib
```

---

## Usage

Run the main pipeline:

```bash
python main_pipeline.py
```

---

## Output

The processed EMG signals are visualized and saved as images.

---

## Note

The dataset is not included in this repository.  
Users can provide their own EMG data in the specified format.
