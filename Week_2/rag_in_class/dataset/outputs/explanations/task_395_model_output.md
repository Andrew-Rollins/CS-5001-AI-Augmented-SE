# Model output for task_395

## Model
- devstral-small-2:24b-cloud

## Original Code:

def first_non_repeating_character(str1):
  char_order = []
  ctr = {}
  for c in str1:
    if c in ctr:
      ctr[c] += 1
    else:
      ctr[c] = 1 
      char_order.append(c)
  for c in char_order:
    if ctr[c] == 1:
      return c
  return None

## Refactored Code:

```python
def first_non_repeating_character(str1):
    char_order = []
    character_count = {}
    for character in str1:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
            char_order.append(character)
    for character in char_order:
        if character_count[character] == 1:
            return character
    return None
```

- Renamed `ctr` to `character_count` for clarity while preserving functionality
- Renamed `c` to `character` in loops for better readability
- Maintained all original logic and operators exactly as in the original
- Kept the same return structure (returning the first non-repeating character or None)
- Preserved the exact same dictionary and list operations
- All function names and arguments remain unchanged
- The core algorithm (tracking character counts and order) is identical
- No mathematical formulas or operators were altered
- The exact same edge cases (empty string, all repeating characters) are handled
