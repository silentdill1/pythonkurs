def create_polynom(coefficients_list):
    def poly(t):
        value = 0
        for i in range(len(coefficients_list)):
            value += t**i * coefficients_list[i]
        return value
    return poly

