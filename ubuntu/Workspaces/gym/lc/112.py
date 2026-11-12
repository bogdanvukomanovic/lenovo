from typing import Optional

from ds.BinaryTree import BinaryTree, TreeNode


class Solution:

    def f(self, root: Optional[TreeNode], targetSum: int, currentSum: int) -> bool:

        if root is None:
            return False

        if root.left is None and root.right is None:
            return targetSum == currentSum + root.val

        return self.f(root.left, targetSum, currentSum + root.val)  \
            or self.f(root.right, targetSum, currentSum + root.val)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root is None:
            return False

        return self.f(root, targetSum, 0)


tree, targetSum = BinaryTree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22
print(Solution().hasPathSum(tree.root, targetSum))
