import random
import matplotlib.pyplot as plt

# Roll a dice 20,000 times
throws = [random.randint(1, 6) for _ in range(100000)]

# Create a histogram of the results
plt.hist(throws, bins=6, edgecolor='black', density=True)

# Set labels for the X, Y axes and the title
plt.xlabel('Dice Roll Results')
plt.ylabel('Relative Frequency')
plt.title('Distribution of Dice Rolls (100,000 trials)')

# Show the plot
plt.show()
