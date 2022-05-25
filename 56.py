from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        new_intervals = []
        for interval in intervals:
            if not len(new_intervals):
                new_intervals.append(interval)
            else:
                last = new_intervals.pop()

                if last[1] >= interval[0]:
                    new_intervals.append([last[0], max(interval[1], last[1])])
                else:
                    new_intervals += [last, interval]
        return new_intervals
