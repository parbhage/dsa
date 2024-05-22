#Addition of long positive integers using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def display(self):
        current = self.head
        while current:
            print(current.data, end="")
            current = current.next
        print()

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def add(self, num2):
        result = LinkedList()
        carry = 0
        current1 = self.head
        current2 = num2.head

        while current1 or current2 or carry:
            val1 = current1.data if current1 else 0
            val2 = current2.data if current2 else 0
            sum_val = val1 + val2 + carry
            carry = sum_val // 10
            result.insert_at_end(sum_val % 10)

            if current1:
                current1 = current1.next
            if current2:
                current2 = current2.next

        return result

# Example usage:
num1 = LinkedList()
num1.insert_at_end(9)
num1.insert_at_end(9)
num1.insert_at_end(9)
num1.display()

num2 = LinkedList()
num2.insert_at_end(1)
num2.insert_at_end(9)
num2.display()

num1.reverse()
num2.reverse()

result = num1.add(num2)
result.reverse()

print("Result:")
result.display()
