import random

class Solution(object):
    def smallestUniqueSubarray(self, nums):
        n = len(nums)
        mod = (1 << 61) - 1
        base = random.randint(100001, 1000000)

        p = [1] * (n + 1)
        h = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = (p[i] * base) % mod
            h[i + 1] = (h[i] * base + nums[i]) % mod

        def has_unique(length):
            pw = p[length]
            seen = set()
            dup = set()
            for i in range(n - length + 1):
                val = (h[i + length] - h[i] * pw) % mod
                if val in seen:
                    dup.add(val)
                else:
                    seen.add(val)
            return len(seen) > len(dup)

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if has_unique(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo