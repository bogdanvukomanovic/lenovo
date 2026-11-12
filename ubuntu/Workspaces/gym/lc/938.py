from typing import Optional

from ds.BinaryTree import *

class Solution:

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        if root == None:
            return 0

        return (root.val if low <= root.val <= high else 0) + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

tree = BinaryTree([10, 5, 15, 3, 7, None, 18])
print(Solution().rangeSumBST(tree.root, 7, 15))
