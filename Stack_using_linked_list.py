# Stack using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            popped_data = self.top.data
            self.top = self.top.next
            return popped_data

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            return self.top.data

    def display(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage:
stack = Stack()

print("Is the stack empty?", stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:")
stack.display()
print("Peek:", stack.peek())

popped_element = stack.pop()
print("Popped element:", popped_element)
print("Stack after pop:")
stack.display()
