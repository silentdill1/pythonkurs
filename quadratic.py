
import sys
import math

# Accept floats a, b and c as command-line arguments. Compute the
# the zeros of the function f(x) = ax^2 + bx + c using the quadratic
# formula.


def zero(a, b, c):
    try:
        if a == 0:
            if b == 0:
                if c == 0:
                    return 'any x-value'
                else:
                    raise Exception('constant function has no zeros')
            else:
                return -c/b
        else:
            b = b/a

            discriminant = b*b - 4.0*c
            if discriminant < 0:
                raise Exception('only imaginary results')
            d = math.sqrt(discriminant)
            return (-b + d) / 2.0, (-b - d) / 2.0

    except Exception as e:
        print(e)
        return 'ERROR'


print(zero(1, 1, 10))


