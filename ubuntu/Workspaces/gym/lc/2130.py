from typing import Optional

from ds.ds import *

class Solution:

    def pairSum(self, head: Optional[ListNode]) -> int:
        
        x, n = head, 0
        while x:
            n += 1
            x = x.next
        
        x = head
        for _ in range(n // 2 - 1):
            x = x.next
        
        z, x = x, x.next

        p = None
        while x:
            y = x.next
            x.next = p
            x, p = y, x

        z.next = p 

        x = head
        for _ in range(n // 2):
            x = x.next
        
        result = 0
        while x:
            result = max(result, head.val + x.val)
            head, x = head.next, x. next

        return result


x4 = ListNode(1)
x3 = ListNode(2, x4)
x2 = ListNode(4, x3)
x1 = ListNode(5, x2)

print(Solution().pairSum(x1))
