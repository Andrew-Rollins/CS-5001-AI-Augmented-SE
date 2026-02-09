def parallel_lines(line1, line2):
    """Check if two lines are parallel by comparing their slopes.

    Args:
        line1: A tuple representing the first line in (y-intercept, slope) form.
        line2: A tuple representing the second line in (y-intercept, slope) form.

    Returns:
        bool: True if the lines are parallel (slopes are equal), False otherwise.
    """
    return line1[0] / line1[1] == line2[0] / line2[1]
