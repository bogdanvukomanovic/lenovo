from typing import List, Optional

class TreeNode:

    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:

    def __init__(self, values: [int]) -> None:
        self.root = self.create(values)

    def create(self, values: List[Optional[int]]) -> Optional[TreeNode]:

        if len(values) == 0:
            return None

        root = TreeNode(values[0])
        queue, values = [root], values[1:]

        while True:

            node, queue = queue[0], queue[1:]

            try:

                left = values.pop(0)
                if left != None:
                    node.left = TreeNode(left)
                    queue.append(node.left)

                right = values.pop(0)
                if right != None:
                    node.right = TreeNode(right)
                    queue.append(node.right)

            except: break

        return root

    def height(self) -> int:

        def f(node: TreeNode) -> int:

            if node == None:
                return 0

            return 1 + max(f(node.left), f(node.right))

        return f(self.root)

    def values(self) -> List[Optional[int]]:

        values = []
        queue = [self.root]

        while len(queue) > 0:

            node = queue.pop(0)
            values.append(node.val if node else None)

            if node:
                queue.append(node.left)
                queue.append(node.right)

        return values
