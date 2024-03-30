import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from random import randint

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
global x 
x = [0]
y = [0]


def animate(i):
    x += x[len(x)-1] + 1
    y += randint(0,10)
    ax1.clear
    ax1.plot(x,y)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

