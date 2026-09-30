class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            digit = 1 << i
            if n & digit:
                res += 1
        return res