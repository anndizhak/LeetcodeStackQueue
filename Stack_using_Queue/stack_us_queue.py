"""Implementing Stack using Queue"""
class Queue:
    """Basic FIFO (First-In-First-Out) queue implementation."""
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def enqueue(self, x):
        """Add an element to the back of the queue."""
        self.items.append(x)

    def dequeue(self):
        """Remove and return the front element."""
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def peek(self):
        """Return the front element without removing it."""
        if self.is_empty():
            return None
        return self.items[0]
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of elements in the queue."""
        return len(self.items)
class MyStack:
    """LIFO stack implementation using a single queue."""
    def __init__(self):
        self.queue = Queue()
    
    def push(self, x):
        """Push element x onto stack."""
        self.queue.enqueue(x)
        for _ in range(self.queue.size()-1):
            self.queue.enqueue(self.queue.dequeue())

    def pop(self):
        """Remove the element on top of the stack and return it."""
        return self.queue.dequeue()
    
    def top(self):
        """Get the top element."""
        return self.queue.peek()
    
    def empty(self):
        """Return whether the stack is empty."""
        return self.queue.is_empty()