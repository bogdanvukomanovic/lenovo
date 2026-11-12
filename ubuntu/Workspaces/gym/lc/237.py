from ds.ds import ListNode

class Solution:
    
    def deleteNode(self, node: ListNode) -> None:
        node.val = node.next.val
        node.next = node.next.next

x4 = ListNode(4)
x3 = ListNode(3, x4)
x2 = ListNode(2, x3)
x1 = ListNode(1, x2)

Solution().deleteNode(x2)

x1.print()