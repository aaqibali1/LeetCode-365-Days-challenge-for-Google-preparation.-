class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        s_len = len(s)
        
        for index, char in enumerate(s):
            if index > s_len / 2:
                return True

            if char != s[s_len - index - 1]:
                return False

        return True