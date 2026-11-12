from typing import Optional

from ds.BinaryTree import *

class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root == None:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

tree = BinaryTree([1, None, 2, 3])
print(Solution().inorderTraversal(tree.root))
