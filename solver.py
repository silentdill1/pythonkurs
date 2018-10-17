class Solver:
    def __init__(self, derivative, interval, initial_values):
        """

        :param derivative: function, returns derivative for timepoint
        :param interval: tuple, start / end timepoint
        :param initial_values: numpy array, array of initial values
        """
        self.derivative = derivative
        self.interval = interval
        self.y = initial_values

    def step(self):
