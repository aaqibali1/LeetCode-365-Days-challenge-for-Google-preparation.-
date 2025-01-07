class Solution:
    def maxProduct(self, nums):
        curProd = 1
        maxProd = float('-inf')  # Equivalent to INT_MIN in C++
        
        # Traverse from left to right
        for num in nums:
            curProd *= num
            maxProd = max(maxProd, curProd)
            if curProd == 0:
                curProd = 1  # Reset if product becomes zero
        
        curProd = 1  # Reset for the right-to-left traversal
        
        # Traverse from right to left
        for num in reversed(nums):
            curProd *= num
            maxProd = max(maxProd, curProd)
            if curProd == 0:
                curProd = 1  # Reset if product becomes zero
        
        return maxProd
