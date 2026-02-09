# Model output for task_153

## Model
- devstral-small-2:24b-cloud

## Original Code:

def parabola_vertex(a, b, c): 
  vertex=(((-b / (2 * a)),(((4 * a * c) - (b * b)) / (4 * a))))
  return vertex

## Refactored Code:

```python
def parabola_vertex(a, b, c):
    x_vertex = (-b) / (2 * a)
    y_vertex = ((4 * a * c) - (b * b)) / (4 * a)
    vertex = (x_vertex, y_vertex)
    return vertex
```

- Retained the exact formula for x_vertex calculation: (-b) / (2 * a)
- Retained the exact formula for y_vertex calculation: ((4 * a * c) - (b * b)) / (4 * a)
- Split the calculation into separate variables for better readability
- Maintained the same return structure (tuple with x and y coordinates)
- Preserved all function arguments (a, b, c) exactly as they were
- Did not modify any operators or mathematical operations
- Kept the function name identical to the original
- Ensured the code path remains exactly the same as validated by tests
