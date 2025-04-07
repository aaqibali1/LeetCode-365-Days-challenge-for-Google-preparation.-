class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Use 32-bit mask to simulate integer overflow behavior
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        
        while b != 0:
            # carry: common bits of a and b
            carry = (a & b) & MASK
            # a becomes XOR of a and b (sum without carry)
            a = (a ^ b) & MASK
            # carry is added to a by shifting it left by 1
            b = (carry << 1) & MASK

        # if a is greater than max int, it's a negative number in 32-bit
        return a if a <= MAX_INT else ~(a ^ MASK)
