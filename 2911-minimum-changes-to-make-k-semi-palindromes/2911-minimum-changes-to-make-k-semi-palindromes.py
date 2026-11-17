class Solution(object):
    def minimumChanges(self, s, k):
        n = len(s)
        divs = [[] for _ in range(n + 1)]
        for d in range(1, n):
            for length in range(d * 2, n + 1, d):
                divs[length].append(d)
        
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                min_ch = float('inf')
                for d in divs[length]:
                    ch = 0
                    for r in range(d):
                        left = i + r
                        right = i + r + ((length - 1 - r) // d) * d
                        while left < right:
                            if s[left] != s[right]:
                                ch += 1
                            left += d
                            right -= d
                    if ch < min_ch:
                        min_ch = ch
                cost[i][j] = min_ch
                
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        for p in range(1, k + 1):
            for i in range(p * 2, n + 1):
                for j in range((p - 1) * 2, i - 1):
                    if dp[j][p - 1] != float('inf'):
                        dp[i][p] = min(dp[i][p], dp[j][p - 1] + cost[j][i - 1])
                        
        return dp[n][k]