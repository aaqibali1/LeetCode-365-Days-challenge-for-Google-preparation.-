class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        position_map = {char: (i // 5, i % 5) for i, char in enumerate("abcdefghijklmnopqrstuvwxyz")}
        x0, y0 = 0, 0
        result = []
        for char in target:
            x, y = position_map[char]
            if y < y0:
                result.append('L' * (y0 - y))
            if x < x0:
                result.append('U' * (x0 - x))
            if x > x0:
                result.append('D' * (x - x0))
            if y > y0:
                result.append('R' * (y - y0))
            result.append('!')
            x0, y0 = x, y
        return "".join(result)
