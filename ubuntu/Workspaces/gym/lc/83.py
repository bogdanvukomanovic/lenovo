from typing import Optional

from ds.ds import ListNode

class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        x = head

        while x:
                      
            y = x
            
            while y.next and y.val == y.next.val:
                y = y.next
            
            x.next = y.next
            x = x.next

        return head


x7 = ListNode(4)
x6 = ListNode(2, x7)
x5 = ListNode(1, x6)
x4 = ListNode(1, x5)
x3 = ListNode(1, x4)
x2 = ListNode(1, x3)
x1 = ListNode(1, x2)

Solution().deleteDuplicates(x1).print()