from collections import deque

class Solution:
    def highestPeak(self, w):
        n, m = len(w), len(w[0])
        ans = [[-1] * m for _ in range(n)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()

        for i in range(n):
            for j in range(m):
                if w[i][j] == 1:
                    ans[i][j] = 0
                    q.append((i, j))

        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and ans[nx][ny] == -1:
                    ans[nx][ny] = ans[x][y] + 1
                    q.append((nx, ny))

        return ans
