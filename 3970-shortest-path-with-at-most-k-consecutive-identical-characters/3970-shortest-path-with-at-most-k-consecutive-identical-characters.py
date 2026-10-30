import heapq
from collections import defaultdict
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
        
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        pq = [(0, 0, 1)]
        
        while pq:
            d, u, count = heapq.heappop(pq)
            if u == n - 1:
                return d
            if d > dist[u][count]:
                continue
            for v, w in graph[u]:
                new_count = count + 1 if labels[u] == labels[v] else 1
                if new_count <= k and d + w < dist[v][new_count]:
                    dist[v][new_count] = d + w
                    heapq.heappush(pq, (d + w, v, new_count))
        
        return -1