from scipy.stats import ttest_1samp

# Producer's claimed mean speed
claimed_mean_speed = 350  # in milliseconds

# Data for Group 2
data_group_2 = [
    395, 420, 408, 385, 405, 398,
    410, 420, 395, 392, 400, 408,
    415, 385, 398, 410, 385, 402,
    415, 398, 405, 390, 402, 410,
    395, 420, 392, 385, 400, 415
]

# Significance level
alpha = 0.05

# Performing a one-sample t-test
t_statistic, p_value = ttest_1samp(data_group_2, claimed_mean_speed)

# Hypothesis testing output
t_statistic, p_value