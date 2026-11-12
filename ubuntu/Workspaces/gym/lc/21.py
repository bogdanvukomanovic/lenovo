from typing import Optional

from ds.ds import ListNode

class Solution:
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None and list2 is None:
            return None

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

x3 = ListNode(4)
x2 = ListNode(2, x3)
x1 = ListNode(1, x2)

y3 = ListNode(4)
y2 = ListNode(3, y3)
y1 = ListNode(1, y2)

solution = Solution()
solution.mergeTwoLists(x1, y1).print()