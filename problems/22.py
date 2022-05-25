from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(n):

            if n == 0:
                yield ''
                return

            if n == 1:
                yield '()'
                return

            for i in range(n):
                for head in generate(i):
                    for tail in generate(n - 1 - i):
                        yield '(' + head + ')' + tail

        return list(generate(n))
