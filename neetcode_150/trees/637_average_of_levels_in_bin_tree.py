from typing import Optional, List
from tree_node import TreeNode


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
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

            level_sum = sum(level)
            level_avg = level_sum / level_count

            q = q[level_count:]
            res.append(level_avg)

        return res