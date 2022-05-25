class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = 1 if n > 0 else -1
        n = abs(n)

        if n == 0:
            return 1

        tail = 1
        current = x

        while n > 1:
            if n % 2 == 1:
                tail *= current

            current *= current

            n = n // 2

        current *= tail

        if sign < 0:
            return 1 / current

        return current
