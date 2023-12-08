import numpy as np
import matplotlib.pyplot as plot
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

# mean
mean_mouse = np.mean(mouse)
mean_joystick = np.mean(joystick)
print("The sample mean rounded to 2 decimals for target group 1 is " + str(np.round(mean_mouse,2)) + "ms. So on average every one of the observation needs "+ str(np.round(mean_mouse,2))+". For the second target group related to joysticks we have a sample mean of: " + str(round(mean_joystick, 2))+ "ms. Thus on average every observation is expected to have a target selection speed of " + str(round(mean_joystick, 2)) + ".")

# variance
var_mouse = round(np.var(mouse), 3)
var_joystick = round(np.var(joystick), 3)

#print("The calculated variance for target group 1 with the mouse rounded to 3 decimals is: " + str(var_mouse)+  "ms. For the second target group related to the joysticks we receive a variance of: " + str(var_joystick))

# standard deviation
std_mouse = round(np.std(mouse), 3)
std_joystick = round(np.std(joystick), 3)

# print("The standard deviation for the first target group with the mouse rounded to 3 decimals is: " + str(std_mouse) + ". Thus the expected observation time could vary around " + str(std_mouse) + "ms. For the second target group, also rounded to 3 decimals, we receive a standard deviation of: " + str(std_joystick) + "ms. Hence the same story for the joystick group. The actual value can vary from the expected duration at a value around: " + str(std_joystick) + "ms.")

#5 number summary
#Mouse group
median_mouse = np.median(mouse)
q1_mouse = np.percentile(mouse, 25)
q3_mouse = np.percentile(mouse, 75)
min_m = np.min(mouse)
max_m = np.max(mouse)

# print("The first 25 percent of the dataset are represented by the value: "+ str(q1_mouse) + ". That means that the upper 25 percent, thus the fastest regarding target selection, need " + str(q1_mouse) + "ms and less for their target selection with the mouse.")
# print("The median of the set, thus the 50th percentile is represented by "+ str(median_mouse) + ". That means that the half of the dataset needs around " + str(median_mouse) + "ms or less in order to select their targets witht the mouse.")
# print("The first 75 percent are represented by the value "+ str(q3_mouse) + ". That means that 75 percent need around" + str(q3_mouse) + "ms or less in order to select their target with the mouse.")
# print("The slowest in the whole group is the observation of " + str(max_m) + "ms.")
# print("The fastest in the whole group is the observation of " + str(min_m) + "ms.")


#Joystick group
median_joystick = np.median(joystick)
q1_joystick = np.percentile(joystick, 25)
q3_joystick = np.percentile(joystick, 75)
min_j = np.min(joystick)
max_j = np.max(joystick)

# print("The first 25 percent of the dataset are represented by the value: "+ str(q1_joystick) + ". That means that the upper 25 percent, thus the fastest regarding target selection, need " + str(q1_joystick) + "ms and less for their target selection with the joystick.")
# print("The median of the set, thus the 50th percentile is represented by "+ str(median_joystick) + ". That means that the half of the dataset needs around " + str(median_joystick) + "ms or less in order to select their targets with the joystick.")
# print("The first 75 percent are represented by the value "+ str(q3_joystick) + ". That means that 75 percent need around" + str(q3_joystick) + "ms or less in order to select their target with the joystick.")
# print("The slowest in the whole group is the observation of " + str(max_j) + "ms.")
# print("The fastest in the whole group is the observation of " + str(min_j) + "ms.")

#####################################################

#Number 2
#Skewness mouse array
print("For the skewness of this graph, so the relation between mean and median, we realize that the distribution is skewed to the left since the mean is smaller than the median. That shows that it's more probable to observe a duration that exceeds the average duration of target selection for the mouse group.")
#Skewness joystick array
print(median_joystick)
print(mean_joystick)
print("For the skewness of the joystick group's observations we find that it's more probable to make observations that exceed the 50th percentile, thus the median, since the average is higher than the 50th percentile.")

#Number 3 Histogram

#Group 1&2
histo_mouse, bin_edges_mouse = np.histogram(mouse, bins=[380, 390, 400, 410, 420])
histo_joystick, bin_edges_joystick = np.histogram(joystick, bins=[380, 390, 400, 410, 420])
#plot it
# plot.hist(mouse, bins=bin_edges_mouse, alpha=0.5, label='Mouse Data')
# plot.hist(joystick, bins=bin_edges_joystick, alpha=0.5, label='Joystick Data')
# plot.xlabel('Milliseconds')
# plot.ylabel('Frequency')
# plot.legend()
# plot.show()

#Number 4
data_to_plot = [mouse, joystick]
labels = ["Group 1", "Group 2"]

labels = ['Group 1', 'Group 2']

# Create the boxplot
plot.figure(figsize=(8, 6))
plot.boxplot(data_to_plot, labels=labels, notch=True, vert=True, patch_artist=True)


# Customize the plot
plot.title('Dispersion Comparison between Group 1 and Group 2')
plot.xlabel('Groups')
plot.ylabel('Milliseconds')

plot.grid(True)
plot.show()