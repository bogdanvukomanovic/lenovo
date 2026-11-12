from ds.BinaryTree import *

class Solution:

    def postorder(self, node: TreeNode) -> (int, int):

        if node == None:
            return (0, 0)

        s1, n1 = self.postorder(node.left)
        s2, n2 = self.postorder(node.right)

        s, n = s1 + s2 + node.val, n1 + n2 + 1

        if s // n == node.val:
            self.result += 1

        return (s, n)

    def averageOfSubtree(self, root: TreeNode) -> int:

        self.result = 0
        self.postorder(root)

        return self.result

tree = BinaryTree([4, 8, 5, 0, 1, None, 6])
print(Solution().averageOfSubtree(tree.root))
