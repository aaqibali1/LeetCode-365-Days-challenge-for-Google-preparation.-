class Solution:
    def minZeroArray(self, nums, queries):
        if all(x == 0 for x in nums):
            return 0
        
        l, r, res = 0, len(queries) - 1, -1
        while l <= r:
            mid = (l + r) // 2
            pref = [0] * (len(nums) + 1)
            
            for i in range(mid + 1):
                li, ri, val = queries[i]
                pref[li] += val
                if ri + 1 < len(pref):
                    pref[ri + 1] -= val
            
            for i in range(1, len(nums)):
                pref[i] += pref[i - 1]
            
            if all(nums[i] <= pref[i] for i in range(len(nums))):
                res = mid + 1
                r = mid - 1
            else:
                l = mid + 1
        
        return res