from typing import Optional

from ds.ds import ListNode

import math

class Solution:
    
    def reorderList(self, head: Optional[ListNode]) -> None:
    
        n = 0
        
        x = head
        while x:
            n += 1
            x = x.next

        x = head
        for _ in range(math.ceil(n/2) - 1):
            x = x.next

        y = x.next
        previous = None

        while y:
            next = y.next
            y.next = previous
            previous = y
            y = next
        
        x.next = previous
        
        y = x.next
        x.next = None
        x = head

        for _ in range(math.ceil(n/2) - n % 2):
            x_temp = x.next
            y_temp = y.next

            x.next = y
            y.next = x_temp

            x = x_temp
            y = y_temp

x5 = ListNode(5)
x4 = ListNode(4, x5)
x3 = ListNode(3, x4)
x2 = ListNode(2, x3)
x1 = ListNode(1, x2)

Solution().reorderList(x1)
x1.print()