"""Implementation of FreqStack"""

from collections import deque
class FreqStack:
    """Stack that removes the most frequent element, then the most recent."""
    def __init__(self):
        """Initializer"""
        self.freq = {}
        self.part = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        """Push a value and update its frequency group."""
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1

        times = self.freq[val]
        if times > self.max_freq:
            self.max_freq = times

        if times not in self.part:
            self.part[times] = deque()
        self.part[times].append(val)
        
    def pop(self) -> int:
        """Remove and return the most frequent element."""
        val = self.part[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.part[self.max_freq]:
            self.max_freq -= 1
        return val