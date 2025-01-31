class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.size = [1] * n  # Size is public for easy access

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])  # Path compression
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Already in the same set
        
        if self.size[root_x] > self.size[root_y]:
            self.size[root_x] += self.size[root_y]
            self.root[root_y] = root_x
        else:
            self.size[root_y] += self.size[root_x]
            self.root[root_x] = root_y
        
        return True  # Merged two disjoint sets

class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        uf = UnionFind(n * n)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def index(x, y):
            return x * n + y
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            uf.union(index(i, j), index(ni, nj))
        
        max_island = max(uf.size) if any(grid[i][j] == 1 for i in range(n) for j in range(n)) else 1
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    total_size = 1
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            root = uf.find(index(ni, nj))
                            if root not in seen:
                                seen.add(root)
                                total_size += uf.size[root]
                    max_island = max(max_island, total_size)
        
        return max_island

if __name__ == "__main__":
    param_1 = [[1, 0], [0, 1]]  # Replace with actual test input
    ret = Solution().largestIsland(param_1)
    print(ret)
