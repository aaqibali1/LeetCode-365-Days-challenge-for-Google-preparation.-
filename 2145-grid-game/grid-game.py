class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        top = sum(grid[0])
        bottom = 0
        result = float('inf')
        
        for i in range(N):
            top -= grid[0][i]
            secondRobot = max(top, bottom)
            result = min(result, secondRobot)
            bottom += grid[1][i]
        
        return result