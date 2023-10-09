def is_balanced(expression):
    stack = []
    for char in expression:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack:
                return False
            top = stack.pop()
            if char == ')' and top != '(':
                return False
            if char == ']' and top != '[':
                return False
            if char == '}' and top != '{':
                return False
    return len(stack) == 0

# Example usage:
expression1 = "({})[]"
expression2 = "([)]"
expression3 = "{[()]}"
expression4 = "{[(])}"

print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
print(is_balanced(expression3))  # Output: True
print(is_balanced(expression4))  # Output: False
