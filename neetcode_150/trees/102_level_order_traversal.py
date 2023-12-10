from typing import Optional, List
from tree_node import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = [root]

        while q:
            level = []
            level_count = len(q)
            for i in range(len(q)):
                level.append(q[i].val)
                if q[i].left:
                    q.append(q[i].left)
                if q[i].right:
                    q.append(q[i].right)

            q = q[level_count:]
            res.append(level)

        return res