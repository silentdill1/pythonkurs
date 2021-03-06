from gsolver import GaussianSolver
from gsolver import IterationsException
import numpy as np


def gaussian_integration(derivative, initial_values, time_interval, rel_tolerance=10**(-4), p_tolerance=10**(-16), error_estimation_method=1):
    """
    integrates given ode system using the gaussian method
    :param derivative: function, returns derivative for time point
    :param time_interval: tuple, start / end time point
    :param initial_values: numpy array, array of initial values
    :param rel_tolerance: float, relative tolerance for integration step
    :param p_tolerance: float, p size in relation to time step size for method1
    :param error_estimation_method: integer, error estimation method of ode solver
    :return: numpy array, time points used
             numpy array, y values calculated
    """

    solver = GaussianSolver(derivative, time_interval, initial_values, rel_tolerance, p_tolerance, error_estimation_method)
    time_points = np.array(time_interval[0])
    y_values = np.empty((1, 2))
    y_values[0] = initial_values
    current_time_point = time_interval[0]
    while current_time_point < time_interval[1]:
        try:
            current_time_point = solver.step(current_time_point)
            time_points = np.append(time_points, current_time_point)
            a_y = np.empty((1, 2))
            a_y[0] = solver.y
            y_values = np.append(y_values, a_y, axis=0)
        except IterationsException as e:
            print(e)
            break
    return time_points, y_values
