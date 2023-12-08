import numpy as np
from scipy.stats import chi2

# Data for Group 1
data_group_1 = [
    420, 395, 412, 380, 405, 415,
    395, 408, 390, 410, 402, 395,
    405, 420, 390, 410, 395, 385,
    408, 402, 415, 400, 420, 390,
    405, 410, 415, 395, 402, 410
]

# Calculating the sample standard deviation
std_dev_group_1 = np.std(data_group_1, ddof=1)

# Sample size
n = len(data_group_1)

# Degrees of freedom
df = n - 1

# Confidence level
alpha = 0.01  # For 99% confidence interval

# Chi-squared distribution values for the confidence interval
chi2_lower = chi2.ppf(alpha / 2, df)
chi2_upper = chi2.ppf(1 - alpha / 2, df)

# Calculating the confidence interval for the standard deviation
conf_interval_lower = np.sqrt((df * std_dev_group_1 ** 2) / chi2_upper)
conf_interval_upper = np.sqrt((df * std_dev_group_1 ** 2) / chi2_lower)

conf_interval_lower, conf_interval_upper