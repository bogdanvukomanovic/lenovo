# Definition for singly-linked list.
class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):

        node = self

        while True:
            
            if node == None:
                break
            
            print(node.val, end = " ")
            node = node.next
        
        print()

class MonotonicStack():

    def __init__(self, elements: [int], increasing: bool = True) -> None:
        self.monotonic_stack = []
        self.increasing = increasing
        self.size = len(elements)

        self.build(elements)

    def build(self, elements: [int]) -> None:

        for element in elements:
            self.push(element)

    def pop(self) -> int:
        self.size -= 1
        return self.monotonic_stack.pop()

    def push(self, element: int) -> None:
    
        self.size += 1

        if len(self.monotonic_stack) == 0:
            self.monotonic_stack.append(element)
            return

        order = (lambda x : x < self.monotonic_stack[-1]) \
            if self.increasing else (lambda x : x > self.monotonic_stack[-1])

        while len(self.monotonic_stack) > 0 and order(element):
            self.monotonic_stack.pop()

        self.monotonic_stack.append(element)
        
    def get_size(self) -> int:
        return self.size

    def __str__(self) -> str:
        return str(self.monotonic_stack)