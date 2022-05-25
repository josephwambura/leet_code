from bisect import bisect_left
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):

            if res and num == res[-1][0]:
                continue

            for j in range(i + 1, len(nums)):
                num_two = nums[j]

                if res and num_two == res[-1][1] and num == res[-1][0]:
                    continue

                pos = bisect_left(nums, -num - num_two, lo=j + 1)

                if 0 <= pos < len(nums) and nums[pos] == -num - num_two:
                    res.append([num, num_two, -num - num_two])

        return res



