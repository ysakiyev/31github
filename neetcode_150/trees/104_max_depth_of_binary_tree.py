from typing import Optional
from tree_node import TreeNode

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthRec(root, 0)

    def maxDepthRec(self, root: Optional[TreeNode], depth: int) -> int:
        if root is None:
            return depth

        return max(self.maxDepthRec(root.left, depth + 1), self.maxDepthRec(root.right, depth + 1))


