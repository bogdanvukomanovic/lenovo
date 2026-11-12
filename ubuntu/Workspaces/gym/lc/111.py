from typing import Optional

from ds.BinaryTree import *


class Solution:

    def f(self, root: Optional[TreeNode], level: int) -> int:

        if root == None:
            return float("inf")

        if root and root.left == None and root.right == None:
            return level

        level += 1

        return min(self.f(root.left, level), self.f(root.right, level))

    def minDepth(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0

        return self.f(root, 1)

tree = BinaryTree([3, 9, 20, None, None, 15, 7])
print(Solution().minDepth(tree.root))
