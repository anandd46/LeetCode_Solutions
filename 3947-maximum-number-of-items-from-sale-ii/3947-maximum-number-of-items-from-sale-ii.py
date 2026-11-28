class Solution(object):
    def maximumSaleItems(self, items, budget):
        n = len(items)
        freq = [0] * (n + 1)
        min_price = items[0][1]
        for f, p in items:
            freq[f] += 1
            if p < min_price:
                min_price = p

        mult = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f]:
                total = 0
                for m in range(f, n + 1, f):
                    total += freq[m]
                mult[f] = total

        items.sort(key=lambda x: x[1])
        ans = 0
        limit = min_price * 2

        for f, p in items:
            if p >= limit or budget < p:
                break
            gain = mult[f] - 1
            if gain > 0:
                take = budget // p
                if take > gain:
                    take = gain
                ans += take * 2
                budget -= take * p

        ans += budget // min_price
        return ans