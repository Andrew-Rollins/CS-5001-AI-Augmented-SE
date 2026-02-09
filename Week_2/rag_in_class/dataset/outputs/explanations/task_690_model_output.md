# Model output for task_690

## Model
- devstral-small-2:24b-cloud

## Original Code:

def mul_consecutive_nums(nums):
    result = [b*a for a, b in zip(nums[:-1], nums[1:])]
    return result

## Refactored Code:

```python
def mul_consecutive_nums(nums):
    """Multiply each pair of consecutive numbers in the input list.

    Args:
        nums: List of numbers to process

    Returns:
        List of products of consecutive pairs
    """
    result = [b * a for a, b in zip(nums[:-1], nums[1:])]
    return result
```

- Retained the exact function name `mul_consecutive_nums`
- Preserved the original list comprehension logic exactly
- Maintained the same zip operation with slice notation `nums[:-1]` and `nums[1:]`
- Kept the multiplication order `b * a` as in original
- Added docstring for clarity without changing functionality
- No changes to operators or mathematical operations
- Function signature remains identical
- All code paths preserved exactly as in original implementation
