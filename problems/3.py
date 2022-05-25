class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = []
        max_n = 0
        for letter in s:
            if letter not in longest_substring:
                longest_substring.append(letter)
            else:
                max_n = max(max_n, len(longest_substring))
                index = longest_substring.index(letter)
                longest_substring = longest_substring[index + 1:]
                longest_substring.append(letter)
        return max(max_n, len(longest_substring))