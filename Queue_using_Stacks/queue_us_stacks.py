"""Implementation Queue using Stacks"""
class Stack:
    """Basic LIFO (Last-In-First-Out) stack implementation."""
    def __init__(self):
        """init"""
        self.items = []

    def push(self, x):
        """Appending element"""
        self.items.append(x)

    def pop(self) -> int:
        """Removing element"""
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            return None
        temp = self.items.pop()
        self.items.append(temp)
        return temp

    def is_empty(self):
        """Return the number of elements in the stack."""
        return len(self.items) == 0

    def size(self):
        """get the length"""
        return len(self.items)

class MyQueue:
    """FIFO (First-In-First-Out) queue implementation using two stacks."""
    def __init__(self):
        """init"""
        self.stack_in = Stack()
        self.stack_out = Stack()

    def push(self, x: int) -> None:
        """Add an element to the back of the queue."""
        self.stack_in.push(x)

    def _moving(self):
        """Transfer elements from input stack to output stack if empty."""
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())

    def pop(self) -> int:
        """Remove and return the front element."""
        self._moving()
        return self.stack_out.pop()

    def peek(self) -> int:
        """Return the front element without removing it."""
        self._moving()
        return self.stack_out.peek()

    def empty(self) -> bool:
        """Check if the queue is empty."""
        return self.stack_in.is_empty() and self.stack_out.is_empty()
