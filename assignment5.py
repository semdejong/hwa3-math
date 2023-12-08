import numpy as np
from scipy.stats import skew, kurtosis, probplot
import matplotlib.pyplot as plt

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


# Calculating Skewness and Kurtosis for both groups
skewness_group_1 = skew(mouse)
kurtosis_group_1 = kurtosis(mouse, fisher=False)  # Fisher=False for standard kurtosis
skewness_group_2 = skew(joystick)
kurtosis_group_2 = kurtosis(joystick, fisher=False)

# Standard Error for Skewness and Kurtosis
n1 = len(mouse)
n2 = len(joystick)
se_skewness_group_1 = np.sqrt(6 / n1)
se_kurtosis_group_1 = np.sqrt(24 / n1)
se_skewness_group_2 = np.sqrt(6 / n2)
se_kurtosis_group_2 = np.sqrt(24 / n2)

# Generating normal QQ plots for both groups
plt.figure(figsize=(12, 6))

# QQ plot for Group 1
plt.subplot(1, 2, 1)
probplot(mouse, dist="norm", plot=plt)
plt.title('Normal QQ Plot for Group 1 (Mouse)')

# QQ plot for Group 2
plt.subplot(1, 2, 2)
probplot(joystick, dist="norm", plot=plt)
plt.title('Normal QQ Plot for Group 2 (Joystick)')

# Display the plots
plt.show()

(skewness_group_1, se_skewness_group_1, kurtosis_group_1, se_kurtosis_group_1), \
(skewness_group_2, se_skewness_group_2, kurtosis_group_2, se_kurtosis_group_2)