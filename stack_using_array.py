#Stack using array
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")

    def size(self):
        return len(self.stack)

# Example usage:
stack = Stack()

print("Is the stack empty?", stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.stack)
print("Size of stack:", stack.size())
print("Peek:", stack.peek())

popped_element = stack.pop()
print("Popped element:", popped_element)
print("Stack after pop:", stack.stack)
