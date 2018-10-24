from gint import gaussian_integration
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from scipy.optimize import curve_fit
from copy import deepcopy

POLYNOMIAL_DEGREE = 10

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

'''
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
            print('tl',tl[i],'ts',ts[j])
            if tl[i] == ts[j]:
                mutual_time_points.append(ts[i])
                mutual_time_point_indices.append((j, i))
                break
            if ts[j] > tl[i]:
                break
    y_value_differences = []
    for indexPair in mutual_time_point_indices:
        y_value_differences.append(yl[indexPair[0]] - ys[indexPair[1]])
    return mutual_time_points, y_value_differences
'''


def polynomial(t, coefficients_list):
    y = 0
    for i in range(len(coefficients_list)):
        y += coefficients_list[i] * t ** i
    return y


def vectorial_field(t, list_of_coefficients_lists):
    x = np.empty(list_of_coefficients_lists.shape[0])
    for i in range(len(list_of_coefficients_lists)):
        x[i] = polynomial(t, list_of_coefficients_lists[i])
    return x


def polynomial_fit(xa, ta, xb, tb):
    if isinstance(xa.shape, tuple) and (xa.shape[1] == xb.shape[1]):
        xa = np.transpose(xa)
        xb = np.transpose(xb)
        coefficients_a = np.empty((xa.shape[0], POLYNOMIAL_DEGREE+1))
        coefficients_b = np.empty((xb.shape[0], POLYNOMIAL_DEGREE+1))
        for variableIndex in range(xa.shape[0]):
            coefficients_a[variableIndex] = np.polyfit(ta, xa[variableIndex], POLYNOMIAL_DEGREE)
        li = []
        for t in ta:
            li.append(vectorial_field(t, coefficients_a)[1])
        fig = plt.figure()
        plot = fig.add_subplot(111)
        plot.plot(ta, li)
        #plot.plot(ta, xa[1])
        fig.savefig('bla.png')
        for variableIndex in range(xb.shape[0]):
            coefficients_b[variableIndex] = np.polyfit(tb, xb[variableIndex], POLYNOMIAL_DEGREE)
        li2 = []
        for t in tb:
            li2.append(vectorial_field(t, coefficients_b)[1])
        plot.plot(tb, li2, label='fit')
        #plot.plot(tb, xb[1], label='function')
        fig.legend()
        return coefficients_a, coefficients_b
    elif isinstance(xa.shape, int) and (xa.shape[1] == xb.shape[1]):
        coefficients_a = np.polyfit(ta, xa, POLYNOMIAL_DEGREE)
        coefficients_b = np.polyfit(tb, xb, POLYNOMIAL_DEGREE)
        return coefficients_a, coefficients_b
    else:
        raise Exception('ndarrays have different second dimensions:'+str(xa.shape)+' and '+str(xb.shape))


def compare_solutions(xa, ta, xb, tb, tm):
    # try:
    coefficients_a, coefficients_b = polynomial_fit(xa, ta, xb, tb)
    time_point_number = len(tm)
    if isinstance(xa.shape, tuple):
        variable_number = coefficients_a.shape[0]
        difference = np.empty((time_point_number, variable_number))
        for t_index in range(time_point_number):
                t = tm[t_index]
                difference[t_index] = vectorial_field(t, coefficients_a) - vectorial_field(t, coefficients_b)
        return difference
    elif isinstance(xa.shape, int):
        difference = np.empty(time_point_number)
        for t_index in range(time_point_number):
            t = tm[t_index]
            difference[t_index] = polynomial(t, coefficients_a) - polynomial(t, coefficients_b)
        return difference
    '''
    except Exception as e:
        print(e)
        return 'ERROR'
    '''

'''
def reshape_acc_variables(array):
    """
    reorders array vector v(t) into arrays v1(t), v2(t) etc.
    :param array: numpy array, representing vector in time course
    :return: numpy array, reshaped
    """
    num_var = array.shape[1] # number of variables
    len_rs = array.shape[0] / num_var # length of reshaped array
    reshaped_array = np.empty((num_var, len_rs))
    for variable_index in range(num_var):
        for time_point in range(len_rs):
            var_arr = reshaped_array[variable_index] # values for time point for variable index
            current_index = time_point * num_var + variable_index  # index of time point in flattened array
            var_arr = np.append(var_arr, array.flat[current_index])
    return reshaped_array
'''


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
# vgl mit odeint:
xDiff = []
yDiff = []
for i in range(0, len(yValues3)):
    xDiff.append(yValues3[i][0]-yValues2[i][0])
    yDiff.append(yValues3[i][1]-yValues2[i][1])
plot.plot(timePoints3, yDiff, label='y diff')
plot.plot(timePoints3, xDiff, label='x diff')
'''
xDiff = []
yDiff = []
difference = compare_solutions(yValues, timePoints, yValues3, timePoints3, timePoints)
for x in difference:
    xDiff.append(x[0])
    yDiff.append(x[1])
plot.plot(timePoints, yDiff, label='y diff')
plot.plot(timePoints, xDiff, label='x diff')
fig.legend()
plt.show()
