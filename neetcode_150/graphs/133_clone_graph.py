from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloned_node = Node(node.val)
        visited_1 = set()
        q1 = deque()
        q2 = deque()

        hmap = {node: cloned_node}

        q1.append(node)
        q2.append(cloned_node)

        while q1:
            node_1 = q1.pop()
            node_2 = q2.pop()

            if node_1 in visited_1:
                continue

            visited_1.add(node_1)

            for neighbor in node_1.neighbors:
                if neighbor in hmap:
                    new_node = hmap[neighbor]
                else:
                    new_node = Node(neighbor.val)
                    hmap[neighbor] = new_node

                node_2.neighbors.append(new_node)

                q1.append(neighbor)
                q2.append(new_node)

        return cloned_node


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

s = Solution()
s.cloneGraph(node1)
