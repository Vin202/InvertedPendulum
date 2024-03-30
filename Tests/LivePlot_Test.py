import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from random import randint
import numpy as np

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
x = [0]
y = [0]
x_interval = 0.1


def animate(i):
    x.append(x[len(x)-1] + x_interval)
    y.append(np.sin(x[len(x)-1]))
    ax1.clear
    ax1.plot(x,y, color='black')

ani = animation.FuncAnimation(fig, animate, interval=1)
plt.show()

