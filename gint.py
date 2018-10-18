from gsolver import GaussianSolver
from gsolver import IterationsException
import numpy as np


def gaussian_integration(derivative, initial_values, time_interval, rel_tolerance=10**(-4), error_estimation_method=1):
    """
    integrates given ode system using the gaussian method
    :param derivative: function, returns derivative for time point
    :param time_interval: tuple, start / end time point
    :param initial_values: numpy array, array of initial values
    :param rel_tolerance: float, relative tolerance for integration step
    :param error_estimation_method: integer, error estimation method of ode solver
    :return: numpy array, time points used
             numpy array, y values calculated
    """

    solver = GaussianSolver(derivative, time_interval, initial_values, rel_tolerance, error_estimation_method)
    time_points = np.array(time_interval[0])
    y_values = np.array(initial_values)
    current_time_point = time_interval[0]
    while current_time_point < time_interval[1]:
        try:
            current_time_point = solver.step(current_time_point)
            time_points = np.append(time_points, current_time_point)
            y_values = np.append(y_values, solver.y)
        except IterationsException as e:
            print(e)
            break
    return time_points, y_values
