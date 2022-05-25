from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        start, i, s, walked = 0, 0, 0, 0

        while walked != len(gas):
            if gas[i] + s - cost[i] >= 0:
                walked += 1
                s += gas[i] - cost[i]
                i = (i + 1) % len(gas)

            elif walked == 0:
                assert i == start
                start += 1
                i = start
                s = 0
            else:
                walked -= 1
                s += cost[start] - gas[start]
                start += 1

            if start == len(gas):
                return -1

        return start


