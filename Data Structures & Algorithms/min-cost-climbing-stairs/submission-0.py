class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a , b = cost[-2], cost[-1]

        for i in reversed(range(len(cost) - 2)):
            c = cost[i]
            tmp = a
            a = c + min(a, b)
            b = tmp


        return min(a, b)
