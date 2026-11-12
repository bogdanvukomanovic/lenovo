from typing import Optional

from ds.ds import ListNode

class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if n == 0:
            return head

        count = 0

        x = head
        while x:
            count += 1
            x = x.next

        if count == n:
            return head.next

        x = head
        for _ in range(count - n - 1):
            x = x.next

        x.next = x.next.next

        return head

x5 = ListNode(5)
x4 = ListNode(4, x5)
x3 = ListNode(3, x4)
x2 = ListNode(2, x3)
x1 = ListNode(1, x2)

n = 0

Solution().removeNthFromEnd(x1, n).print()