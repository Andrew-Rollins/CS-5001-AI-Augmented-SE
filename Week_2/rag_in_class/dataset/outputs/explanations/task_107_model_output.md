# Model output for task_107

## Model
- devstral-small-2:24b-cloud

## Original Code:

def count_Hexadecimal(L,R) :  
    count = 0;  
    for i in range(L,R + 1) : 
        if (i >= 10 and i <= 15) : 
            count += 1;  
        elif (i > 15) : 
            k = i;  
            while (k != 0) :  
                if (k % 16 >= 10) : 
                    count += 1;  
                k = k // 16;  
    return count;  

## Refactored Code:

```python
def count_Hexadecimal(L, R):
    count = 0
    for i in range(L, R + 1):
        if 10 <= i <= 15:
            count += 1
        elif i > 15:
            k = i
            while k != 0:
                if k % 16 >= 10:
                    count += 1
                k = k // 16
    return count
```

- Retained the exact function name `count_Hexadecimal`
- Preserved the original logic for counting hexadecimal digits (10-15) in the range [L, R]
- Maintained the same loop structure and conditions
- Kept the same variable names (count, i, k)
- Preserved the exact mathematical operations (%, //)
- Did not fix any potential bugs (e.g., the condition `i > 15` could be `i >= 16` but was left unchanged)
- Improved readability by removing unnecessary parentheses and semicolons
- Maintained the exact same return statement
- Ensured all code paths remain identical to the original implementation
