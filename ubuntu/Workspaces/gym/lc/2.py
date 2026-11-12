from typing import Optional

from ds.ds import ListNode

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode()
        digit = result

        carry = 0
        while l1 or l2:

            sum = 0
            
            if l1: sum += l1.val

            if l2: sum += l2.val
            
            sum += carry

            carry = 0 if sum < 10 else 1
            digit.next = ListNode(sum if sum < 10 else sum % 10)

            digit = digit.next

            if l1: l1 = l1.next

            if l2: l2 = l2.next

            if l1 and not l2 and carry == 0:
                break
            if l2 and not l1 and carry == 0:
                break
                
        if carry == 0:
            digit.next = l1 if l1 else l2 if l2 else None
        else:
            digit.next = ListNode(carry)

        return result.next

x3 = ListNode(3)
x2 = ListNode(4, x3)
x1 = ListNode(2, x2)

y3 = ListNode(4)
y2 = ListNode(6, y3)
y1 = ListNode(5, y2)

Solution().addTwoNumbers(x1, y1).print()