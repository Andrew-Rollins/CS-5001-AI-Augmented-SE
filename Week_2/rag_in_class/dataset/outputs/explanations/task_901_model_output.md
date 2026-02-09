# Model output for task_901

## Model
- devstral-small-2:24b-cloud

## Original Code:

def smallest_multiple(n):
    if (n<=2):
      return n
    i = n * 2
    factors = [number  for number in range(n, 1, -1) if number * 2 > n]
    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
            if (a == factors[-1] and i % a == 0):
                return i

## Refactored Code:

```python
def smallest_multiple(n):
    if n <= 2:
        return n
    i = n * 2
    factors = [number for number in range(n, 1, -1) if number * 2 > n]
    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
            if a == factors[-1] and i % a == 0:
                return i
```

- Retained the exact logic and structure of the original function
- Improved indentation and spacing for better readability
- Kept the same variable names and function signature
- Preserved all operators and mathematical expressions exactly as they were
- Maintained the same loop and conditional structures
- Ensured the function still returns the same values for the same inputs
- Did not fix any potential bugs or logical errors
- Kept the same list comprehension syntax and logic
- Preserved the exact same control flow paths
