# Model output for task_681

## Model
- devstral-small-2:24b-cloud

## Original Code:

def smallest_Divisor(n): 
    if (n % 2 == 0): 
        return 2; 
    i = 3;  
    while (i*i <= n): 
        if (n % i == 0): 
            return i; 
        i += 2; 
    return n; 

## Refactored Code:

```python
def smallest_Divisor(n):
    if n % 2 == 0:
        return 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return n
```

- Removed unnecessary parentheses around conditions
- Removed semicolons at the end of statements
- Improved indentation consistency
- Maintained all original logic and operators exactly as they were
- Preserved the exact same function name and signature
- Kept the same mathematical operations and conditions
- Ensured no changes to the algorithm's behavior
- Retained all original variable names and their usage
