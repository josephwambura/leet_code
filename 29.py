class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == -1 and dividend == (-1 << 31):
            return (1 << 31) - 1

        negative = (dividend > 0) ^ (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)

        if divisor > dividend:
            return 0

        dividend = [int(x) for x in bin(dividend)[2:]]
        res = 0
        rest = 0

        while dividend:
            rest += dividend.pop(0)
            res += res

            if rest >= divisor:
                rest -= divisor
                res += 1

            rest += rest

        if negative:
            res = -res
        return res
