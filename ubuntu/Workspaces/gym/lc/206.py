from typing import Optional

from ds.ds import ListNode

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        previous = None

        while head:
            
            x = head.next
            head.next = previous
            head, previous = x, head

        return previous
    

x5 = ListNode(5)
x4 = ListNode(4, x5)
x3 = ListNode(3, x4)
x2 = ListNode(2, x3)
x1 = ListNode(1, x2)

solution = Solution()
solution.reverseList(x1).print()