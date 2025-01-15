class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        a = bin(num1).count('1')
        b = bin(num2).count('1')
        res = num1
        for i in range(32):
            if a > b and (num1 & (1 << i)):
                res ^= (1 << i)
                a -= 1
            elif a < b and not (num1 & (1 << i)):
                res ^= (1 << i)
                a += 1
        return res
