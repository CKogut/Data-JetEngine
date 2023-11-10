import matplotlib.pyplot as plt

# Style
plt.style.use('seaborn-v0_8')

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()
#ax.scatter(x_values, y_values, c="purple", s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set title and axes labels
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for the axes
ax.axis([0, 1100, 0, 1100000])

#plt.show()
#plt.savefig('square_plot.png', bbox_inches='tight')