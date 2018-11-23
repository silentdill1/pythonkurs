import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, odeint

DENSITY = 25
LOWER_BOUND = 0
UPPER_BOUND = 13

numbers = np.linspace(LOWER_BOUND, UPPER_BOUND, DENSITY)
grid = np.zeros((DENSITY, DENSITY, 2))
for i, number1 in enumerate(numbers):
    for j, number2 in enumerate(numbers):
        grid[i, j] = np.array([number1, number2])

a = 1.5
b = 1
d = 1
g = 4


def f(t, y):
    dy_dt = np.zeros(2)
    y1 = y[0]
    y2 = y[1]
    dy_dt[0] = a*y1 - b*y2*y1
    dy_dt[1] = d*y1*y2 - g*y2
    return dy_dt


def wrapper(y, t):
    return f(t, y)


t = np.linspace(0, 5, 1000)
solution = solve_ivp(f, (0, 5), (10, 5), t_eval=t)
values = odeint(wrapper, (10, 5), t)
fig = plt.figure()
plot = fig.add_subplot(111)
for line in grid:
    for entry in line:
        deriv = f(0, entry)
        plot.quiver(entry[0], entry[1], deriv[0], deriv[1], color='orange', headwidth=10, headlength=10,
                    scale=200, scale_units='xy', width=1.5*10**(-3))
print(solution.y[0])
plot.plot(solution.y[0], solution.y[1])
plot.plot(values[:, 0], values[:, 1])
plt.show()


