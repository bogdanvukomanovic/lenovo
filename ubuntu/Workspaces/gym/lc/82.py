from typing import Optional

from ds.ds import ListNode

class Solution:
    
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        result = ListNode()
        x = result

        while head and head.next:
            
            if head.val == head.next.val:
                value = head.val
                while head and head.val == value:
                    head = head.next
    
            else:
                x.next = head
                x = x.next

                head = head.next
                x.next = None

        if head:
            x.next = head    

        return result.next

x7 = ListNode(5)
x6 = ListNode(4, x7)
x5 = ListNode(4, x6)
x4 = ListNode(3, x5)
x3 = ListNode(3, x4)
x2 = ListNode(2, x3)
x1 = ListNode(1, x2)

Solution().deleteDuplicates(x1).print()