from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        r = [nums[0]]
        for i in range(1, len(nums)):
            odd = r[i - 2] if i > 1 else 0
            r.append(max(r[i - 1], odd + nums[i]))

        return r[-1]
