class Stack:
    def __init__(self, max_size):
        self._max_size = max_size
        self.stack = []

    def get_max_size(self):
        return self._max_size

    def is_full(self):
        if len(self.stack) == self._max_size:
            return True
        else:
            return False

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, value):
        if self.is_full():
            return False
        else:
            self.stack.append(value)
            return True

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def top(self):
        if self.is_empty():
            return ''
        else:
            return self.stack[-1]


def is_valid(string):
    stack = Stack(n)
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in mapping:
            top_element = stack.pop()
            if mapping[char] != top_element:
                return 'invalid'

        else:
            stack.push(char)

    if stack.is_empty():
        return 'valid'
    else:
        return 'invalid'


n = int(input())
string = input()
print(is_valid(string))
