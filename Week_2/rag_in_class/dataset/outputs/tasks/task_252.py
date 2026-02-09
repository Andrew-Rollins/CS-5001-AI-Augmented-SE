import cmath

def convert(numbers):
    """Convert a complex number to its polar form representation.

    Args:
        numbers: A complex number to be converted to polar form.

    Returns:
        A tuple containing the magnitude and phase (in radians) of the complex number.
    """
    polar_representation = cmath.polar(numbers)
    return polar_representation
