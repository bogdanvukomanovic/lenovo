from typing import Optional

from ds.ds import ListNode

class Solution:

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        L = ListNode()
        R = ListNode()

        result = L
        connect = R
        
        while head:

            if head.val < x:
                L.next = head
                L = head
            else:
                R.next = head
                R = head
            
            head = head.next

        L.next = None
        R.next = None
        L.next = connect.next

        return result.next

x6 = ListNode(2)
x5 = ListNode(5, x6)
x4 = ListNode(2, x5)
x3 = ListNode(3, x4)
x2 = ListNode(4, x3)
x1 = ListNode(1, x2)

x2 = ListNode(1)
x1 = ListNode(2, x2)

Solution().partition(x1, 2).print()