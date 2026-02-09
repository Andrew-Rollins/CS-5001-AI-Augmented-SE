# Model output for task_397

## Model
- devstral-small-2:24b-cloud

## Original Code:

def median_numbers(a,b,c):
 if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
 else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c
 return median

## Refactored Code:

```python
def median_numbers(a, b, c):
    if a > b:
        if a < c:
            median = a
        elif b > c:
            median = b
        else:
            median = c
    else:
        if a > c:
            median = a
        elif b < c:
            median = b
        else:
            median = c
    return median
```

- Retained all original function names and arguments exactly as provided
- Preserved all conditional logic and comparison operators without modification
- Maintained the exact same code structure and flow control
- Kept all variable names unchanged
- Ensured the return statement remains identical
- Did not alter any mathematical comparisons or conditions
- Preserved the original indentation and code organization
- Did not introduce any new logic or remove any existing logic
- Maintained all original comments (none present in this case)
- Ensured the function signature remains exactly the same
