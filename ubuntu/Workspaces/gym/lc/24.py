from typing import Optional

from ds.ds import ListNode

class Solution:

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head

        R = head.next

        P = ListNode(next = head)

        while head and head.next:
            
            X = head.next

            head.next = X.next
            X.next = head
            P.next = X

            P = head
            head = head.next

        return R

x6 = ListNode(6)
x5 = ListNode(5, x6)
x4 = ListNode(4, x5)
x3 = ListNode(3, x4)
x2 = ListNode(2, x3)
x1 = ListNode(1, x2)

Solution().swapPairs(x1).print()