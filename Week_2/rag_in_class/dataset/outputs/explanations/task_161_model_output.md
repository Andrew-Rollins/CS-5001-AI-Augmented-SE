# Model output for task_161

## Model
- devstral-small-2:24b-cloud

## Original Code:

def remove_elements(list1, list2):
    result = [x for x in list1 if x not in list2]
    return result

## Refactored Code:

```python
def remove_elements(list1, list2):
    """Remove elements from list1 that are present in list2.

    Args:
        list1: The list from which elements will be removed.
        list2: The list containing elements to remove from list1.

    Returns:
        A new list containing only elements from list1 that are not in list2.
    """
    result = [x for x in list1 if x not in list2]
    return result
```

- Retained the exact function name `remove_elements`
- Preserved the original logic and list comprehension structure
- Added docstring to improve readability without changing functionality
- Maintained the same argument names and order
- Kept the exact same return statement
- No changes to the list membership check operator (`not in`)
- No modifications to the list iteration or filtering logic
- Preserved the original variable name `result`
- No changes to the return value structure
