from typing import Optional
from tree_node import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diam = [0]
        def dfs(node):
            if node is None:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)
            max_diam[0] = max(max_diam[0], left + right + 2)

            return max(left, right) + 1
        dfs(root)
        return max_diam[0]
