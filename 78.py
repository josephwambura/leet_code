from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = [[]]
        for num in nums:
            sets += [x + [num] for x in sets]

        return sets
