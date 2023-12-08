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


plt.figure(figsize=(8, 6))

# Creating the boxplot
plt.boxplot([mouse, joystick], labels=['Group 1 - Mouse', 'Group 2 - Joystick'])

# Adding titles and labels
plt.title('Combined Boxplot of Target Selection Speeds')
plt.ylabel('Target Selection Speed (milliseconds)')

# Display the plot
plt.show()