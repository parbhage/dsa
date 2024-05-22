#Queue using array
class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return item

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        temp_front = self.front
        temp_rear = self.rear
        while temp_front != temp_rear:
            print(self.queue[temp_front], end=" <- ")
            temp_front = (temp_front + 1) % self.capacity
        print(self.queue[temp_rear])


# Example usage:
queue = Queue(5)

print("Is the queue empty?", queue.is_empty())

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print("Queue:")
queue.display()

dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)
print("Queue after dequeue:")
queue.display()

