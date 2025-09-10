class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # step 1: remove leading spaces
        if not s:
            return 0

        sign = 1
        if s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            s = s[1:]

        num = 0
        for ch in s:
            if not ch.isdigit():
                break
            num = num * 10 + int(ch)

        num *= sign

        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num
