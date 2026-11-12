from typing import Optional

from ds.ds import *

class Solution:

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        while head and head.val == val:
            head = head.next

        c, p = head, None
        while c:

            if c.val == val:
                p.next = c.next
            else:
                p = c

            c = c.next

        return head

x7 = ListNode(6)
x6 = ListNode(5, x7)
x5 = ListNode(4, x6)
x4 = ListNode(6, x5)
x3 = ListNode(1, x4)
x2 = ListNode(3, x3)
x1 = ListNode(6, x2)
Solution().removeElements(x1, 6).print()
