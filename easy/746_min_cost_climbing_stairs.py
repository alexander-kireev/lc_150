class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev_prev = cost[0]
        prev = cost[1]

        for i in range(2, len(cost)):
            cur = min(prev_prev + cost[i], prev + cost[i])
            prev_prev = prev
            prev = cur
        
        return min(prev, prev_prev)