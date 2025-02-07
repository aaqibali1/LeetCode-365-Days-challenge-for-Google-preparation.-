from collections import defaultdict

class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        mpp = defaultdict(set)
        mp = {}
        ans = []

        for ball, color in queries:
            if ball not in mp:
                mp[ball] = color
                mpp[color].add(ball)
            else:
                c = mp[ball]
                mpp[c].remove(ball)
                if not mpp[c]:
                    del mpp[c]
                mp[ball] = color
                mpp[color].add(ball)
            ans.append(len(mpp))

        return ans