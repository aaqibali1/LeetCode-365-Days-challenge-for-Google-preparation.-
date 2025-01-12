class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        def check(s, locked, left, right):
            balance = 0
            for i in range(len(s)):
                if locked[i] == '0' or s[i] == left:
                    balance += 1
                else:
                    balance -= 1
                if balance < 0:
                    return False
            return True
        
        return check(s, locked, '(', ')') and check(s[::-1], locked[::-1], ')', '(')