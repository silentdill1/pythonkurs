import numpy as np


class GaussianSolver:
    def __init__(self, derivative, initial_values, interval, rel_tolerance, error_estimation_method=1):
        """
        :param derivative: function, returns derivative for timepoint
        :param interval: tuple, start / end timepoint
        :param initial_values: numpy array, array of initial values
        """
        self.derivative = derivative
        self.y = initial_values
        self.max_time_step = interval[1] - interval[0]
        self.rtol = rel_tolerance
        self.errEstMet = error_estimation_method

    def estimate_error1(self, t, h):
        """
        :param t: float, current time point
        :param h: float, time step
        :return: error estimate, tolerance, current y change
        """
        dy_dt = self.derivative(self.y, t)
        p = h * 10**(-15)
        dyi = dy_dt * h
        dyi_p = dy_dt * (h + p)
        err = (dyi_p - dyi - dy_dt*p) / (2*h*p + p**2)
        yi = self.y + dyi
        tol = yi * 10**(-4)
        return err, tol, dyi

    def step(self, time_point):
        """
        does one integration step
        :param time_point: current timepoint
        :return:
        """
        err = np.inf
        time_step = self.max_time_step
        tol = 0
        dyi = 0
        number_of_iterations = 0
        while err > tol and number_of_iterations < 1000:
            time_step = time_step / 100
            err, tol, dyi = self.estimate_error1(time_point, time_step)
            number_of_iterations += 1
        self.y += dyi
        next_time_point = time_point + time_step
        return next_time_point