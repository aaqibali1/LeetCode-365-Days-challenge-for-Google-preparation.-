from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = [1] * n
        right_prod = [1] * n
        result = [0] * n

        # Calculate left product
        for i in range(1, n):
            left_prod[i] = left_prod[i - 1] * nums[i - 1]

        # Calculate right product
        for i in range(n - 2, -1, -1):
            right_prod[i] = right_prod[i + 1] * nums[i + 1]

        # Calculate the result
        for i in range(n):
            result[i] = left_prod[i] * right_prod[i]

        return result
