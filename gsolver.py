import numpy as np


class IterationsException(Exception):
    pass


def has_greater_element(a, b):
    if isinstance(a, np.ndarray):
        for element1 in a:
            for element2 in b:
                if element1 > element2:
                    return True
        return False
    else:
        return a > b


class GaussianSolver:
    def __init__(self, derivative, interval, initial_values, rel_tolerance, p_tolerance, error_estimation_method):
        """
        :param derivative: function, returns derivative for timepoint
        :param interval: tuple, start / end timepoint
        :param rel_tolerance: float, relative tolerance for y value integration step
        :param p_tolerance: float, p size in relation to time step size for method1
        :param error_estimation_method: integer, error estimation method
        """
        self.derivative = derivative
        self.max_time_step = interval[1] - interval[0]
        self.rTol = rel_tolerance
        self.p = p_tolerance * self.max_time_step
        self.errEstMet = error_estimation_method
        self.y = initial_values

    def estimate_error1(self, t, h):
        """
        :param t: float, current time point
        :param h: float, time step
        :return: error estimate, tolerance, current y change
        """
        dy_dt = self.derivative(self.y, t)
        dyi = dy_dt * h
        dyi_p = dy_dt * (h + self.p)
        c = (dyi_p - dyi - dy_dt*self.p) / (2*h*self.p + self.p**2)
        err = c*h**2
        yi = self.y + dyi
        tol = yi * self.rTol
        return err, tol, dyi

    def step(self, time_point):
        """
        does one integration step
        :param time_point: current timepoint
        :return: next time point
        """
        err = np.inf
        time_step = self.max_time_step
        tol = 0
        dyi = 0
        number_of_iterations = 0
        while has_greater_element(err, tol):
            time_step = time_step / 100
            if number_of_iterations > 10**6:
                raise IterationsException('too many iterations, error not converging?')
            if self.errEstMet == 1:
                err, tol, dyi = self.estimate_error1(time_point, time_step)
            number_of_iterations += 1
        self.y += dyi
        next_time_point = time_point + time_step
        return next_time_point
