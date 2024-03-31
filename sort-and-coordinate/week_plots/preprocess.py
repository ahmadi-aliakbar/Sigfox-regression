import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Assuming you have 12 plots named as figure_1.jpg, figure_2.jpg, ..., figure_12.jpg

# Function to update the plot for each frame
def update(frame):
    img = plt.imread('figure_{frame + 1}.png')
    im.set_array(img)
    return im,

# Create a figure and axis
fig, ax = plt.subplots()

# Display the first image
img = plt.imread('figure_1.jpg')
im = ax.imshow(img)

# Hide axis
ax.axis('off')

# Create animation
ani = animation.FuncAnimation(fig, update, frames=12, interval=1000)  # Change interval as needed

# Save the animation as a gif file
ani.save('animation.gif', writer='imagemagick')  # You may need to install imagemagick for this

# Display the animation
plt.show()
