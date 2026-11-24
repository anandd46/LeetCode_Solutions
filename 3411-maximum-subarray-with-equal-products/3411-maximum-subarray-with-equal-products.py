class Solution(object):
    def maxLength(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)
        ans = 0
        for i in range(n):
            p = 1
            g = 0
            l = 1
            for j in range(i, n):
                x = nums[j]
                p *= x
                g = x if g == 0 else gcd(g, x)
                l = (l * x) // gcd(l, x)
                if p == l * g:
                    if j - i + 1 > ans:
                        ans = j - i + 1
        return ans