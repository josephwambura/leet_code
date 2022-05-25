class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        div = 10
        x, n = divmod(x, div)
        res = [n]
        while x > 0:
            x, n = divmod(x, div)
            res.append(n)

        res_n = 0
        for i, r in enumerate(res):
            res_n += 10 ** (len(res) - 1 - i) * r

            if res_n > 2 ** 31 - 1:
                return 0

            if res_n == 2 ** 31 - 1 and sign == 1:
                return 0

        return sign * res_n
