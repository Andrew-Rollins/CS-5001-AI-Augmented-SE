def mul_consecutive_nums(nums):
    """Multiply each pair of consecutive numbers in the input list.

    Args:
        nums: List of numbers to process

    Returns:
        List of products of consecutive pairs
    """
    result = [b * a for a, b in zip(nums[:-1], nums[1:])]
    return result
