import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Roll a dice 100,000 times
throws = [random.randint(1, 6) for _ in range(100000)]

# Create a figure and axis
fig, ax = plt.subplots()

# Set labels for the X, Y axes and the title
ax.set_xlabel('Dice Roll Results')
ax.set_ylabel('Relative Frequency')
ax.set_title('Distribution of Dice Rolls (100,000 trials)')

# Create a histogram for the initial data (empty plot at start)
hist, bins, patches = ax.hist([], bins=6, edgecolor='black', density=True)

def update(frame):
    # Update the histogram as we simulate more dice rolls
    ax.clear()
    ax.set_xlabel('Dice Roll Results')
    ax.set_ylabel('Relative Frequency')
    ax.set_title('Distribution of Dice Rolls (100,000 trials)')
    
    # Update the histogram with results up to the current frame
    ax.hist(throws[:frame], bins=6, edgecolor='black', density=True)

# Create an animation
ani = animation.FuncAnimation(fig, update, frames=range(1, 100001, 1000), interval=10)

# Save the animation as a video
ani.save('dice_rolls_simulation.mp4', writer='ffmpeg', fps=30)

plt.show()
