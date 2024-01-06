from collections import deque
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        rows, cols = len(image), len(image[0])
        init_color = image[sr][sc]

        q = deque()
        q.append([sr, sc])

        while q:
            r, c = q.popleft()
            image[r][c] = color
            adj = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for dr, dc in adj:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < rows and 0 <= new_c < cols and image[new_r][new_c] == init_color:
                    q.append([new_r, new_c])

        return image
