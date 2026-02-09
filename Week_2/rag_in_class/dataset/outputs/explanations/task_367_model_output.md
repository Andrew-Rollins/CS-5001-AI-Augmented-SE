# Model output for task_367

## Model
- devstral-small-2:24b-cloud

## Original Code:

class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
def get_height(root): 
	if root is None: 
		return 0
	return max(get_height(root.left), get_height(root.right)) + 1
def is_tree_balanced(root): 
	if root is None: 
		return True
	lh = get_height(root.left) 
	rh = get_height(root.right) 
	if (abs(lh - rh) <= 1) and is_tree_balanced( 
	root.left) is True and is_tree_balanced( root.right) is True: 
		return True
	return False

## Refactored Code:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def get_height(root):
    if root is None:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1

def is_tree_balanced(root):
    if root is None:
        return True
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    if (abs(left_height - right_height) <= 1) and is_tree_balanced(root.left) is True and is_tree_balanced(root.right) is True:
        return True
    return False
```

- Retained all function names exactly as they were
- Improved variable naming (lh → left_height, rh → right_height) for better readability
- Maintained all existing logic and operators without any changes
- Preserved the exact same code paths and conditions
- Kept the same indentation and structure
- Did not fix any bugs or correct any formulas
- Ensured all function arguments remain unchanged
- Maintained the same return values and conditions
