class Stack:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.list = [None] * (stack_size * 3)
        self.top = [-1, -1, -1]

    def is_empty(self, stack_number):
        return self.top[stack_number] == -1

    def is_full(self, stack_number):
        return self.top[stack_number] == (stack_number + 1) * self.stack_size - 1

    def push(self, item, stack_number):
        if not self.is_full(stack_number):
            self.top[stack_number] += 1
            index = self.top[stack_number] + stack_number * self.stack_size
            self.list[index] = item

    def pop(self, stack_number):
        if not self.is_empty(stack_number):
            index = self.top[stack_number] + stack_number * self.stack_size
            item = self.list[index]
            self.list[index] = None
            self.top[stack_number] -= 1
            return item

# Example usage:
stack = Stack(3)  # Create three stacks with a total size of 9 (3 each)

stack.push(1, 0)  # Push 1 to the first stack
stack.push(2, 0)  # Push 2 to the first stack
stack.push(3, 0)  # Push 3 to the first stack

stack.push(4, 1)  # Push 4 to the second stack
stack.push(5, 1)  # Push 5 to the second stack

stack.push(6, 2)  # Push 6 to the third stack

print(stack.pop(0))  # Output: 3 (Pop from the first stack)
print(stack.pop(1))  # Output: 5 (Pop from the second stack)
print(stack.pop(2))  # Output: 6 (Pop from the third stack)
