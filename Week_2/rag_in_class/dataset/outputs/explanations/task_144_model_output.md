# Model output for task_144

## Model
- devstral-small-2:24b-cloud

## Original Code:

def sum_Pairs(arr,n): 
    sum = 0
    for i in range(n - 1,-1,-1): 
        sum += i*arr[i] - (n-1-i) * arr[i] 
    return sum

## Refactored Code:

```python
def sum_Pairs(arr, n):
    total = 0
    for index in range(n - 1, -1, -1):
        total += index * arr[index] - (n - 1 - index) * arr[index]
    return total
```

- Renamed variable `sum` to `total` to avoid shadowing built-in function
- Renamed loop variable `i` to `index` for better readability
- Kept the exact same mathematical formula and logic
- Preserved all function arguments and return behavior
- Maintained the same loop direction and range
- Ensured no changes to the core calculation logic
- Kept the same function name `sum_Pairs`
