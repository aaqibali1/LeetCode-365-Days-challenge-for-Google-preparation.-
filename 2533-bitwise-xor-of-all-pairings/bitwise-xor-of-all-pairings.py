class Solution:
    def xorAllNums(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        ans = 0

        if n2 % 2 > 0:
            for num in nums1:
                ans ^= num

        if n1 % 2 > 0:
            for num in nums2:
                ans ^= num

        return ans
