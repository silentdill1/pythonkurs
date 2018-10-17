import numpy as np


class GaussianSolver:
    def __init__(self, derivative, initial_values, interval, rel_tolerance):
        """
        creates new Solver object
        :param derivative: function, returns derivative for timepoint
        :param interval: tuple, start / end timepoint
        :param initial_values: numpy array, array of initial values
        """
        self.derivative = derivative
        self.y = initial_values
        self.max_time_step = interval[1] - interval[0]
        self.rtol = rel_tolerance

    def step(self, time_point):
        """

        :param time_point: current timepoint
        :return:
        """
        dy = self.derivative(self.y, time_point)
        err = np.inf
        time_step = self.max_time_step / 100
        tol = 0
        while err > tol:

        next_time_point = time_point + time_step
        return next_time_point
