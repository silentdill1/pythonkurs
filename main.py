from gint import gaussian_integration
import matplotlib.pyplot as plt
import numpy as np
import scipy.inter


def derivative1(y, t):
    dy_dt = -y
    return dy_dt


def derivative2(y, t):
    dy_dt = -np.exp(y)
    return dy_dt


initialValue = np.log(100)
timePoints, yValues = gaussian_integration(derivative2, initialValue, (0, 1))
fig = plt.figure()
plot = fig.add_subplot(111)
plot.plot(timePoints, yValues)
plt.show()