class Solution(object):
    def climbStairs(self, n, costs):
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            c = costs[i - 1]
            min_cost = dp[i - 1] + c + 1
            if i >= 2:
                min_cost = min(min_cost, dp[i - 2] + c + 4)
            if i >= 3:
                min_cost = min(min_cost, dp[i - 3] + c + 9)
            dp[i] = min_cost
            
        return dp[n]