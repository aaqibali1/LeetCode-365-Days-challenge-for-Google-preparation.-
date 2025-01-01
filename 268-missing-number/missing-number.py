class Solution:
    def missingNumber(self, nums):
        # Initialize result with the length of the nums list
        res = len(nums)

        # Iterate through the list, applying XOR with the current index and value
        for i in range(len(nums)):
            res ^= nums[i]
            res ^= i

        return res
