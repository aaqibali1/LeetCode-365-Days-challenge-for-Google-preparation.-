class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = l + (r - l) // 2
            if nums[mid] < nums[l]:
                r = mid
            else:
                l = mid + 1
        return nums[l]
