class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0 
        output = 0  
        for r in range(len(s)): 
            if s[r] in seen and seen[s[r]] >= l:  
                l = seen[s[r]] + 1  
            seen[s[r]] = r  
            output = max(output, r - l + 1) 
        return output
