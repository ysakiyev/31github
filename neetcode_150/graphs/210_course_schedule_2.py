from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {c: [] for c in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        order = []
        visited, cycle = set(), set()

        def dfs(c):
            if c in cycle:
                return False

            if c in visited:
                return True

            cycle.add(c)
            for p in adj[c]:
                if not dfs(p):
                    return False

            cycle.remove(c)
            visited.add(c)
            order.append(c)
            return True

        for course in adj.keys():
            if not dfs(course):
                return []

        return order
