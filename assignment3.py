import numpy as np
import matplotlib.pyplot as plt
# Number 1
mouse = [420, 395, 412, 380, 405, 415,
395, 408, 390, 410, 402, 395,
405, 420, 390, 410, 395, 385,
408, 402, 415, 400, 420, 390,
405, 410, 415, 395, 402, 410,]

joystick = [395, 420, 408, 385, 405, 398,
410, 420, 395, 392, 400, 408,
415, 385, 398, 410, 385, 402,
415, 398, 405, 390, 402, 410,
395, 420, 392, 385, 400, 415]

# Combined Histogram for both groups

plt.figure(figsize=(8, 6))

# Plotting both histograms together
plt.hist(mouse, bins=10, color='blue', alpha=0.7, label='Group 1 - Mouse')
plt.hist(joystick, bins=10, color='green', alpha=0.7, label='Group 2 - Joystick')

# Adding titles and labels
plt.title('Combined Histogram of Target Selection Speeds')
plt.xlabel('Target Selection Speed (milliseconds)')
plt.ylabel('Frequency')
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()