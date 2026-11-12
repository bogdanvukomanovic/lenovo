from typing import Optional

from ds.ds import ListNode

class Solution:
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right:
            return head

        result = head
        
        x = None
        for _ in range(left - 1):
            x = head
            head = head.next
        
        y = head
        
        prev = None
        for _ in range(right - left + 1):
            z = head.next
            head.next = prev
            head, prev = z, head

        if x:
            x.next = prev

        y.next = head

        return result if x else prev 

x5 = ListNode(5)
x4 = ListNode(4, x5)
x3 = ListNode(3, x4)
x2 = ListNode(2, x3)
x1 = ListNode(1, x2)

Solution().reverseBetween(x1, 1, 2).print()