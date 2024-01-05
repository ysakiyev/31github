from typing import Optional
from tree_node import TreeNode


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root and subRoot:
            return False

        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, s, t):
        if not s and not t:
            return True

        if not s or not t:
            return False

        return s.val == t.val and self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
