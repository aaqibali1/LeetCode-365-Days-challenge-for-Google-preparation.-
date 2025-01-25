from typing import List

class Solution:
    def lexicographicallySmallestArray(self, arr: List[int], threshold: int) -> List[int]:
        value_index_pairs = sorted((value, index) for index, value in enumerate(arr))
        grouped_pairs = [[value_index_pairs[0]]]

        for i in range(1, len(arr)):
            if value_index_pairs[i][0] - value_index_pairs[i - 1][0] <= threshold:
                grouped_pairs[-1].append(value_index_pairs[i])
            else:
                grouped_pairs.append([value_index_pairs[i]])

        for group in grouped_pairs:
            indices = sorted(index for _, index in group)
            values = sorted(value for value, _ in group)
            for i, index in enumerate(indices):
                arr[index] = values[i]

        return arr
