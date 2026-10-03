class Solution:
    def combination_helper(self, nums: List[int], current: List[int], 
                            target: int, total: int, 
                            result: List[List[int]]) -> List[List[int]]:
        if total > target:
            return
        elif total == target:
            current.sort()
            if current not in result: result.append(current)
            return
        
        for i, num in enumerate(nums):
            self.combination_helper(nums[i:], current + [num], target,
                                total + num, result)
        
        return result
        


    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.combination_helper(nums, [], target, 0, [])

        