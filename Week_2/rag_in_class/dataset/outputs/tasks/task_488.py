import math

def area_pentagon(a):
    """Calculate the area of a regular pentagon with side length a.

    Args:
        a: Length of a side of the pentagon

    Returns:
        The area of the pentagon using the formula:
        (sqrt(5*(5+2*sqrt(5))) * a^2) / 4
    """
    area = (math.sqrt(5 * (5 + 2 * math.sqrt(5))) * pow(a, 2)) / 4.0
    return area
