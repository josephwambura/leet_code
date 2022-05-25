class Solution:
    def numDecodings(self, s: str) -> int:
        memory = {}

        def decode_number(num_s):
            if num_s in memory:
                return memory[num_s]

            if num_s.startswith('0'):
                return 0

            if len(num_s) <= 1:
                return 1

            if int(num_s[:2]) > 26:
                r = decode_number(num_s[1:])
            else:
                r = decode_number(num_s[1:]) + decode_number(num_s[2:])

            memory[num_s] = r
            return r

        return decode_number(s)
