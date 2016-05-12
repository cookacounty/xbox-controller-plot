import numpy as np
import matplotlib.pyplot as plt


plt.ion()
plt.xlim([-10, 10])
plt.ylim([-10, 10])
    
while True:
    y = np.random.random()*10
    plt.hold(False)
    #plt.scatter(i, y)
    x1=0
    x2=y
    y1=0
    y2=y
    plt.plot([x1, x2], [y1,  y2], '-')
    plt.pause(0.05)
