from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        pairs = sorted([(x + 1, y) for x, y in enumerate(height)], key=lambda i: i[1], reverse=True)
        x_min, x_max = pairs[0][0], pairs[0][0]
        s_best = 0
        for current in pairs[1:]:
            if current[0] > x_max:
                x_max = current[0]
                s_best = max(s_best, current[1] * (x_max - x_min))
            elif current[0] < x_min:
                x_min = current[0]
                s_best = max(s_best, current[1] * (x_max - x_min))
        return s_best