from typing import Optional

from ds.ds import ListNode

class Solution:
    
    # Acquire length of list and then use stack.
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
    #     n = 0

    #     i = head
    #     while i:
    #         n += 1
    #         i = i.next

    #     stack = []
    #     for l in range(n // 2):
    #         stack.append(head.val)
    #         head = head.next
        
    #     if n % 2 == 1:
    #         head = head.next

    #     for r in range(n // 2):
    #         if stack.pop() != head.val:
    #             return False
    #         head = head.next
        
    #     return True
    
    
    # Reverse the second half of list. Use two pointers to compare values.
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        n = 0

        i = head
        while i:
            n += 1
            i = i.next
        
        left = head
        for j in range(n // 2):
            head = head.next
        
        if n % 2 == 1:
            head = head.next
        
        prev = None
        while head:
            x = head.next
            head.next = prev
            prev = head 
            head = x

        right = prev

        for k in range(n // 2):
            
            if left.val != right.val:
                return False
        
            left = left.next
            right = right.next

        return True

x5 = ListNode(1)
x4 = ListNode(2, x5)
x3 = ListNode(5, x4)
x2 = ListNode(2, x3)
x1 = ListNode(1, x2)

print(Solution().isPalindrome(x1))