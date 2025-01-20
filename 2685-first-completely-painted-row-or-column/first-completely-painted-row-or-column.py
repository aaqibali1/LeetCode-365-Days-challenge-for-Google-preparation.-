class Solution:
    def firstCompleteIndex(self, arr, mat):
        n, m = len(mat), len(mat[0])
        rowcol = {mat[i][j]: (i, j) for i in range(n) for j in range(m)}
        row, col = [0] * n, [0] * m
        
        for i, num in enumerate(arr):
            r, c = rowcol[num]
            row[r] += 1
            col[c] += 1
            if row[r] == m or col[c] == n:
                return i
        
        return 0