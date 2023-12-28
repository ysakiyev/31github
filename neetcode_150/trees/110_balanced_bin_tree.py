from typing import Optional
from tree_node import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.height(root.left) + 1
        right = self.height(root.right) + 1

        return max(left, right)

