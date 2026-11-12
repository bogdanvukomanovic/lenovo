from typing import Optional

from ds.BinaryTree import *


class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root

tree = BinaryTree([4,2,7,1,3,6,9])
tree.root = Solution().invertTree(tree.root)
print(tree.values())
