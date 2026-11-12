from typing import Optional

from ds.BinaryTree import *

class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not (p or q):
            return True

        if not (p and q):
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

p = BinaryTree([1, 2])
q = BinaryTree([1, None, 2])
print(Solution().isSameTree(p.root, q.root))
