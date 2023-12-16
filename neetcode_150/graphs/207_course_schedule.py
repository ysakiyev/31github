from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for c1, c2 in prerequisites:
            adj[c1].append(c2)

        v = set()

        def dfs(c: int) -> bool:
            if c in v:
                return False

            if not adj[c]:
                return True

            v.add(c)

            for p in adj[c]:
                if not dfs(p):
                    return False

            v.remove(c)
            adj[c] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True