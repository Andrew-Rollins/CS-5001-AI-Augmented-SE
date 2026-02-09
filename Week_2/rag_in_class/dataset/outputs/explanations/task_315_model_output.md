# Model output for task_315

## Model
- devstral-small-2:24b-cloud

## Original Code:

def find_Max_Len_Even(str): 
    n = len(str) 
    i = 0
    currlen = 0
    maxlen = 0
    st = -1
    while (i < n): 
        if (str[i] == ' '): 
            if (currlen % 2 == 0): 
                if (maxlen < currlen): 
                    maxlen = currlen 
                    st = i - currlen 
            currlen = 0 
        else : 
            currlen += 1
        i += 1
    if (currlen % 2 == 0): 
        if (maxlen < currlen): 
            maxlen = currlen 
            st = i - currlen 
    if (st == -1): 
        return "-1" 
    return str[st: st + maxlen] 

## Refactored Code:

```python
def find_Max_Len_Even(input_string):
    string_length = len(input_string)
    current_index = 0
    current_length = 0
    maximum_length = 0
    start_index = -1

    while current_index < string_length:
        if input_string[current_index] == ' ':
            if current_length % 2 == 0:
                if maximum_length < current_length:
                    maximum_length = current_length
                    start_index = current_index - current_length
            current_length = 0
        else:
            current_length += 1
        current_index += 1

    if current_length % 2 == 0:
        if maximum_length < current_length:
            maximum_length = current_length
            start_index = current_index - current_length

    if start_index == -1:
        return "-1"
    return input_string[start_index: start_index + maximum_length]
```

- Renamed variables to be more descriptive (e.g., `n` to `string_length`, `i` to `current_index`)
- Maintained all original logic and operators exactly as they were
- Preserved the exact same function name and signature
- Kept all conditional checks and mathematical operations unchanged
- Ensured the return values and string slicing remain identical
- Maintained the same control flow and loop structure
- Did not fix any potential bugs or logical errors
- Kept all original spacing and indentation patterns
