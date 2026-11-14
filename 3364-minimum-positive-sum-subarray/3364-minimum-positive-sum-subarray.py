class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        ans = float('inf')
        n = len(nums)
        
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                length = j - i + 1
                if l <= length <= r and current_sum > 0:
                    ans = min(ans, current_sum)
                    
        return ans if ans != float('inf') else -1