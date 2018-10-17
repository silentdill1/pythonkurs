from gsolver import GaussianSolver


def gaussian_integration(derivative, intial_values, time_interval, rel_tolerance):
    """
        integrates given ode system using the gaussian method
        :param derivative: function, returns derivative for timepoint
        :param interval: tuple, start / end timepoint
        :param initial_values: numpy array, array of initial values
    """
    solver = GaussianSolver(derivative, intial_values, time_interval, rel_tolerance)
    solver.step(interval[0])
