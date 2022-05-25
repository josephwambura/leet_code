from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def generate_permutations(nums):
            m = len(nums)
            if m <= 1:
                yield nums
                return

            for i in range(m):
                for combination in generate_permutations(nums[:i] + nums[i + 1:]):
                    yield [nums[i]] + combination

        return list(generate_permutations(nums))

