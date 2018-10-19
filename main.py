from gint import gaussian_integration
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from copy import deepcopy

def derivative1(y, t):
    dy_dt = -y
    return dy_dt


def derivative2(y, t):
    dy_dt = -np.exp(y)
    return dy_dt


def derivative3(n, t):
    y = n[1]
    x = n[0]
    dx_dt = -x + y + np.log(x)
    dy_dt = -y - y**2 + x
    change = np.array([dx_dt, dy_dt])
    return change


def compare_solutions(ya, ta, yb, tb):
    mutual_time_points = []
    mutual_time_point_indices = []
    if len(ta) > len(tb):
        tl = ta
        ts = tb
        yl = ya
        ys = yb
    else:
        tl = tb
        ts = ta
        yl = yb
        ys = ya
    for i in range(0, len(tl)):
        for j in range(0, len(ts)):
            if tl[i] == ts[j]:
                mutual_time_points.append(ts[i])
                mutual_time_point_indices.append((j, i))
    y_value_differences = []
    for indexPair in mutual_time_point_indices:
        y_value_differences.append(yl[indexPair[0]] - ys[indexPair[1]])
    return mutual_time_points, y_value_differences

initialValues = np.array([10.0, 10.0])
initialValues2 = deepcopy(initialValues)
initialValues3 = deepcopy(initialValues)

timePoints3, yValues3 = gaussian_integration(derivative3, initialValues, (0, 1), rel_tolerance=10**(-12))
timePoints2 = timePoints3
timePoints, yValues = gaussian_integration(derivative3, initialValues2, (0, 1), rel_tolerance=10**(-3))
yValues2 = odeint(derivative3, initialValues3, timePoints2)

fig = plt.figure()
plot = fig.add_subplot(111)
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
'''
plot.plot(timePoints, y1, label='y high tolerance')
plot.plot(timePoints, x1, label='x high tolerance')
plot.plot(timePoints2, y2, label='x odeint')
plot.plot(timePoints2, x2, label='y odeint')
plot.plot(timePoints3, y3, label='x low tolerance')
plot.plot(timePoints3, x3, label='y low tolerance')

xDiff = []
yDiff = []
for i in range(0, len(yValues3)):
    xDiff.append(yValues3[i][0]-yValues2[i][0])
    yDiff.append(yValues3[i][1]-yValues2[i][1])
plot.plot(timePoints3, yDiff, label='y diff')
plot.plot(timePoints3, xDiff, label='x diff')
'''

for
xDiff = []
yDiff = []
fig.legend()

plt.show()
