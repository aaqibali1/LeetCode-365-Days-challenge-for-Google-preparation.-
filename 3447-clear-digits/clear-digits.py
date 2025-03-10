class Solution:
    def clearDigits(self, s: str) -> str:
        res = []
        delete_cnt = 0

        for i in reversed(range(len(s))):
            if s[i].isdigit():
                delete_cnt += 1
            elif delete_cnt:
                delete_cnt -= 1
            else:
                res.append(s[i])

        return "".join(res[::-1])  # Reverse back to original order

# Example usage:
solution = Solution()
print(solution.clearDigits("a1b2c3"))  # Output: "abc"
