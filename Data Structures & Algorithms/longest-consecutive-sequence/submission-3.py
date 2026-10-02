class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return 1

        numset = set(nums)
        res = 1

        for n in nums:
            if n - 1 not in numset:
                count = 1
                cur = n + 1
                while cur in numset:
                    count += 1
                    cur += 1
                res = max(res, count)
        return res
        