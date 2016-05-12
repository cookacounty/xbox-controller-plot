"""
Plot I2C 3D Sensor Data
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import sensor3d as s3d
#import time
#import numpy as np

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-1, 1), ylim=(-1, 1))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    #x = [0, np.random.random()*10]
    #y = [0, np.random.random()*10]
    joy.read_angle()
    x=[0, joy.x]
    y=[0, joy.y]
    print("LEFT X/Y",joy.x,joy.y)
    line.set_data(x,y)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               interval=50, blit=True)

# Setup joystick
i2c_addr = 0x60
joy = s3d.Sensor3D(i2c_addr)

# Show the plot, close the joystick if something goes wrong
plt.show()

