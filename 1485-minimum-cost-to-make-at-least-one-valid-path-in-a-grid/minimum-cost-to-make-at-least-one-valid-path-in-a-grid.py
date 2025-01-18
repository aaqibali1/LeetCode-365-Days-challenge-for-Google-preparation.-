from heapq import heappush, heappop
from typing import List

class Solution:
    # Directions: right, left, down, up
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    
    @staticmethod
    def is_outside(i: int, j: int, r: int, c: int) -> bool:
        return i < 0 or i >= r or j < 0 or j >= c

    @staticmethod
    def minCost(grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        dist = [[float('inf')] * c for _ in range(r)]
        visited = [[False] * c for _ in range(r)]
        
        # Min-heap priority queue: (cost, i, j)
        pq = []
        heappush(pq, (0, 0, 0))  # Corrected: Properly closed parenthesis
        dist[0][0] = 0

        while pq:
            d, i, j = heappop(pq)
            if visited[i][j]:
                continue
            visited[i][j] = True

            # Reached destination
            if i == r - 1 and j == c - 1:
                return d

            current_direction = grid[i][j]

            for a in range(4):
                ni, nj = i + Solution.di[a], j + Solution.dj[a]
                
                if Solution.is_outside(ni, nj, r, c) or visited[ni][nj]:
                    continue

                # No extra cost if moving in the preferred direction
                new_d = d + (0 if (a + 1) == current_direction else 1)

                if new_d < dist[ni][nj]:
                    dist[ni][nj] = new_d
                    heappush(pq, (new_d, ni, nj))  # Corrected: Properly closed parenthesis

        return -1  # If no path is found
