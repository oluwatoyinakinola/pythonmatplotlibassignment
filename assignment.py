import matplotlib.pyplot as plt
import numpy as np

# Bivariate data

price = [1000, 670, 200, 1200]
quality = [6, 8, 9, 10]

# Creating a 2D numpy array to store the data

data = np.array([price, quality]).T  

# Plotting the data

plt.scatter(data[:, 1], data[:, 0], label='Data Points')

# Adding legend and labels

plt.legend()
plt.title("Price vs Quality Assessment")
plt.xlabel("Quality")
plt.ylabel("Price")

# Showing the plot

plt.show()
