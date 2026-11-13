from collections import deque

class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        dq = deque()
        ans = 0
        R = n - 1
        sum_pm = 0
        sum_nums = 0
        
        for L in range(n - 1, -1, -1):
            x = nums[L]
            count = 1
            
            while dq and dq[0][0] <= x:
                v, c = dq.popleft()
                sum_pm += (x - v) * c
                count += c
                
            dq.appendleft([x, count])
            sum_pm += x
            sum_nums += x
            
            while sum_pm - sum_nums > k:
                v_r = dq[-1][0]
                sum_pm -= v_r
                sum_nums -= nums[R]
                dq[-1][1] -= 1
                if dq[-1][1] == 0:
                    dq.pop()
                R -= 1
                
            ans += (R - L + 1)
            
        return ans