class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        if len(s) == 1: return 1
        lset = set()
        res = 1
        l = 0
        r = 1
        lset.add(s[l])
        while r < len(s):
            if s[r] not in lset:
                lset.add(s[r])
                r += 1
            else:
                res = max(res, r - l)
                lset.remove(s[l])
                l += 1
        res = max(res, r - l)
        return res
        