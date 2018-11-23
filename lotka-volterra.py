import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

a = 1.5
b = 1
d = 1
g = 4


def f(y,t):
    dy_dt = np.zeros(2)
    y1 = y[0]
    y2 = y[1]
    dy_dt[0] = a*y1 - b*y2*y1
    dy_dt[1] = d*y1*y2 - g*y2
    return dy_dt


time_grid = np.linspace(0, 200, 400)
result = odeint(f, (50, 5), time_grid)
fig = plt.figure()
plot = fig.add_subplot(111)
for i in (0, 1):
    plot.plot(time_grid, result[:, i])
plt.show()