from typing import Optional

from ds.BinaryTree import * 

class Solution:

    def height(self, node: Optional[TreeNode]) -> int:

        if not node:
            return 0

        return 1 + max(self.height(node.left), self.height(node.right))

    def f(self, root: Optional[TreeNode], level: int) -> int:

        if level == 1 and root:
            return root.val

        if not root:
            return 0

        return self.f(root.left, level - 1) + self.f(root.right, level - 1)

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        return self.f(root, self.height(root))

# TODO: Compute sum for every level to avoid traversing the tree twice.

tree = BinaryTree([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None , 8])
print(Solution().deepestLeavesSum(tree.root))
