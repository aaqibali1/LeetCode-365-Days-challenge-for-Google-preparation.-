class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, "", 1)  # Remove first occurrence of part
        return s

# Example usage:
if __name__ == "__main__":
    s = "daabcbaabcbc"
    part = "abc"
    solution = Solution()
    result = solution.removeOccurrences(s, part)
    print("Resulting string:", result)  # Expected Output: "dab"
