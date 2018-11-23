from gint import gaussian_integration
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

A = 1.5
B = 1
C = 1
D = 4


def derivative(x, t):
    dx_dt = x - 0.01*x**2
    return dx_dt


def derivative2(y, t):
    dy_dt = np.zeros(2)
    x1 = y[0]
    x2 = y[1]
    dy_dt[0] = A*x1 - B*x1*x2
    dy_dt[1] = C*x1*x2 - D*x2
    return dy_dt


initialValues = np.array([10.0, 5.0])
timePoints, yValues = gaussian_integration(derivative2, initialValues, (0, 10), rel_tolerance=10**(-2))
yValues2 = odeint(derivative2, initialValues, timePoints)
fig = plt.figure()
print(yValues)
plot = fig.add_subplot(111)
plot.plot(timePoints, yValues[:, 0:1], label='prey')
plot.plot(timePoints, yValues2[:, 0:1], label='prey ode')
plot.plot(timePoints, yValues[:, 1:2], label='hunters')
plot.plot(timePoints, yValues2[:, 1:2], label='hunters ode')
fig.legend()
plt.show()
