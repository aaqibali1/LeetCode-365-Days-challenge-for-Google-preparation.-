class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []

        for candy in candies:
            result.append(candy + extraCandies >= max_candies)
        return result 
        
                   














#   max_candies = max(candies)  # Find the current maximum
#         result = []
#         for candy in candies:
#             result.append(candy + extraCandies >= max_candies)
#         return result

        # max_candies = max(candies)
        # return [c + extraCandies >= max_candies for c in candies]