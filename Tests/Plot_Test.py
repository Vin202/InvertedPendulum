import matplotlib.pyplot as plt
import numpy as np
from time import sleep

import matplotlib.animation as animation

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

plt.ion()
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show(block=True)

sleep(2)
y = y**2
ax.plot(x,y)

