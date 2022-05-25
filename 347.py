from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for element in nums:
            if element in frequency:
                frequency[element] += 1
            else:
                frequency[element] = 1

        frequency = [(x, y) for x, y in frequency.items()]

        def quick_search(array, k_local):
            if not array:
                return []

            pivot = array[0][1]

            left, right, middle = [], [], []
            for el in array:
                if el[1] < pivot:
                    right.append(el)
                elif el[1] > pivot:
                    left.append(el)
                else:
                    middle.append(el)

            if len(left + middle) == k_local:
                return left + middle

            if len(left + middle) < k_local:
                return left + middle + quick_search(right, k_local - len(left + middle))

            if len(left) == k_local:
                return left

            if len(left) > k_local:
                return quick_search(left, k_local)

            k_local -= len(left)
            return left + middle[:k_local]

        sorted_k = quick_search(frequency, k)

        return [x[0] for x in sorted_k]




