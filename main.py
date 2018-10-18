from gint import gaussian_integration
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


def derivative1(y, t):
    dy_dt = -y
    return dy_dt


def derivative2(y, t):
    dy_dt = -np.exp(y)
    return dy_dt


def derivative3(n, t):
    y = n[1]
    x = n[0]
    dx_dt = -x
    dy_dt = -y - y**2
    change = np.array([dx_dt, dy_dt])
    return change


initialValues = np.array([10.0, 10.0])
timePoints2 = np.linspace(0, 1, 101)
timePoints, yValues = gaussian_integration(derivative3, initialValues, (0, 1), rel_tolerance=10**(-3))
yValues2 = odeint(derivative3, initialValues, timePoints2)
timePoints3, yValues3 = gaussian_integration(derivative3, initialValues, (0, 1), rel_tolerance=10**(-12))
fig = plt.figure()
plot = fig.add_subplot(111)
'''
mutualTimePoints = []
mutualTimePointIndices = []
for i in range(0, len(timePoints3)):
    for j in range(0, len(timePoints)):
        if timePoints3[i] == timePoints[j]:
            mutualTimePoints.append(timePoints3[i])
            mutualTimePointIndices.append((j, i))
print(len(timePoints))
print(len(timePoints3))
yValueDifference = []
for indexPair in mutualTimePointIndices:
    yValueDifference.append(yValues[indexPair[0]] - yValues3[indexPair[1]])
plot.plot(mutualTimePoints, yValueDifference)
'''
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
for point in yValues:
    x1.append(point[0])
    y1.append(point[1])
for point in yValues2:
    x2.append(point[0])
    y2.append(point[1])
for point in yValues3:
    x3.append(point[0])
    y3.append(point[1])

plot.plot(timePoints, y1, label='y high tolerance')
plot.plot(timePoints, x1, label='x high tolerance')
plot.plot(timePoints2, y2, label='x odeint')
plot.plot(timePoints2, x2, label='y odeint')
plot.plot(timePoints3, y3, label='x low tolerance')
plot.plot(timePoints3, x3, label='y low tolerance')
fig.legend()

plt.show()
