class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        for i in range(n + 1):
            k = 0
            while i != 0:
                k += (i & 1)
                i = i >> 1
            output.append(k)        
        
        return output