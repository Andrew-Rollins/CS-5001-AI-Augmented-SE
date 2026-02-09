# Model output for task_488

## Model
- devstral-small-2:24b-cloud

## Original Code:

import math
def area_pentagon(a):
  area=(math.sqrt(5*(5+2*math.sqrt(5)))*pow(a,2))/4.0
  return area

## Refactored Code:

```python
import math

def area_pentagon(a):
    """Calculate the area of a regular pentagon with side length a.

    Args:
        a: Length of a side of the pentagon

    Returns:
        The area of the pentagon using the formula:
        (sqrt(5*(5+2*sqrt(5))) * a^2) / 4
    """
    area = (math.sqrt(5 * (5 + 2 * math.sqrt(5))) * pow(a, 2)) / 4.0
    return area
```

- Retained the exact formula from the original implementation
- Added docstring to explain the function's purpose and parameters
- Maintained the same function name and signature
- Kept the same mathematical operations and operators
- Preserved the exact calculation logic
- Used the same variable name 'area' for consistency
- Maintained the same return statement structure
- Kept the same import statement for math module
