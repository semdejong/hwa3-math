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

# Claimed variance
claimed_variance = 200  # in ms^2

# Sample variance for Group 1
sample_variance_group_1 = np.var(data_group_1, ddof=1)

# Sample size and degrees of freedom
n = len(data_group_1)
df = n - 1

# Significance level
alpha = 0.05

# Chi-square test statistic for testing variance
chi_square_stat = (df * sample_variance_group_1) / claimed_variance
p_value = 1 - chi2.cdf(chi_square_stat, df)

chi_square_stat, p_values