from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        def binary_search(left, right):
            if right - left <= 1:
                if nums[right] > nums[left]:
                    return right
                return left

            middle = (left + right) // 2
            if nums[middle - 1] < nums[middle] and nums[middle] > nums[middle + 1]:
                return middle

            if nums[middle - 1] > nums[middle]:
                return binary_search(left, middle - 1)

            return binary_search(middle + 1, right)

        return binary_search(0, len(nums) - 1)



