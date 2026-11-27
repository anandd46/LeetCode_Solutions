class Solution(object):
    def maximumSaleItems(self, items, budget):
        max_f = max(f for f, p in items)
        freq = [0] * (max_f + 1)
        min_price = float('inf')
        for f, p in items:
            freq[f] += 1
            if p < min_price:
                min_price = p

        mult = [0] * (max_f + 1)
        for f in range(1, max_f + 1):
            if freq[f]:
                total = 0
                for m in range(f, max_f + 1, f):
                    total += freq[m]
                mult[f] = total

        dp = [0] * (budget + 1)
        for f, p in items:
            if p <= budget:
                v = mult[f]
                for c in range(budget, p - 1, -1):
                    nv = dp[c - p] + v
                    if nv > dp[c]:
                        dp[c] = nv

        ans = 0
        for c in range(budget + 1):
            val = dp[c] + (budget - c) // min_price
            if val > ans:
                ans = val
        return ans