from gsolver import GaussianSolver
import numpy as np

def gaussian_integration(derivative, initial_values, time_interval, rel_tolerance):
    """
        integrates given ode system using the gaussian method
        :param derivative: function, returns derivative for timepoint
        :param interval: tuple, start / end timepoint
        :param initial_values: numpy array, array of initial values
    """
    solver = GaussianSolver(derivative, intial_values, time_interval, rel_tolerance)
    time_points = np.array(time_interval[0])
    y_values = np.array(initial_values)
    current_time_point = time_interval[0]
    while current_time_point < time_interval[1]:
        time_points = np.append(time_points, current_time_point)
        y_values = np.append(y_values, solver.y)
