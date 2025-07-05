# Stack

A simple stack data structure implemented in Python, with a maximum size.  
Includes an example function (`is_valid`) to check for balanced brackets using the stack.

## Features

- **Fixed maximum stack size**
- **Standard stack operations:** push, pop, top, is_empty, is_full, get_max_size
- **Practical example**: Validates if a string of brackets is balanced (parentheses, square brackets, curly braces)

## Stack Usage Example

```python
from Stack import Stack

s = Stack(5)
s.push(10)
s.push(20)
print(s.top())      # Output: 20
s.pop()
print(s.is_empty()) # Output: False
