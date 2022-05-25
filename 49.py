from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            ordered = ''.join(sorted(s))
            if ordered in groups:
                groups[ordered].append(s)
            else:
                groups[ordered] = [s]

        return list(groups.values())