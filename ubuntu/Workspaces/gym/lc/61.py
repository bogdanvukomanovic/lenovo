from typing import Optional

from ds.ds import ListNode

class Solution:

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head == None:
            return head

        n = 0
        i = head
        while i:
            n += 1
            i = i.next

        r = k % n

        if r == 0:
            return head

        right = head
        for j in range(n - r - 1):
            right = right.next
        
        left = right.next
        result = left
        right.next = None

        for t in range(r - 1):
            left = left.next

        left.next = head

        return result


x5 = ListNode(5)
x4 = ListNode(4, x5)
x3 = ListNode(3, x4)
x2 = ListNode(2, x3)
x1 = ListNode(1, x2)

Solution().rotateRight(x1, 2).print()