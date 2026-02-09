# Model output for task_392

## Model
- devstral-small-2:24b-cloud

## Original Code:

def get_max_sum (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]

## Refactored Code:

```python
def get_max_sum(n):
    result = [0, 1]
    for i in range(2, n + 1):
        result.append(max(i, result[i // 2] + result[i // 3] + result[i // 4] + result[i // 5]))
    return result[n]
```

- Retained the exact function name `get_max_sum`
- Replaced list initialization and append with direct list creation for first two elements
- Replaced while loop with for loop for cleaner iteration
- Kept the same mathematical operations and logic flow
- Maintained the same return value structure
- Preserved all integer division operations (//) as in original
- Kept the same max() comparison logic
- Maintained the same list indexing approach
- Preserved the exact same return statement structure
