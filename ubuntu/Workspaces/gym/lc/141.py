from typing import Optional

from ds.ds import ListNode

class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not (head and head.next):
            return False  
        
        slow = head
        fast = head

        while fast.next and fast.next.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

x3 = ListNode(4)
x2 = ListNode(2, x3)
x1 = ListNode(1, x2)

print(Solution().hasCycle(x1))