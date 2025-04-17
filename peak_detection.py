import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# 1. Generate sample signal data
np.random.seed(42)
x = np.linspace(0, 4 * np.pi, 500)
signal = np.sin(x) + 0.3 * np.random.randn(len(x))  # Sine wave + noise

# 2. Smooth signal using a simple moving average
window_size = 5
smoothed = np.convolve(signal, np.ones(window_size) / window_size, mode='same')

# 3. Detect peaks
peaks, _ = find_peaks(smoothed, height=0.5, distance=20)  # You can tweak these parameters

# 4. Plot
plt.figure(figsize=(12, 6))
plt.plot(x, signal, label='Noisy Signal', alpha=0.4)
plt.plot(x, smoothed, label='Smoothed Signal', linewidth=2)
plt.plot(x[peaks], smoothed[peaks], 'rx', label='Detected Peaks')
plt.legend()
plt.title("Signal Processing & Peak Detection")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
