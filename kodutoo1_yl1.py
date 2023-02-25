class Solution:
    from math import trunc
    def divide(self, dividend: int, divisor: int) -> int:
        x = dividend/divisor
        return trunc(x) #round down