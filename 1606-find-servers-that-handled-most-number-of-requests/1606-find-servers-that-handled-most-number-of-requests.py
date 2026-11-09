import heapq

class Solution(object):
    def busiestServers(self, k, arrival, load):
        available = list(range(k))
        busy = []
        counts = [0] * k
        
        for i, (arr, ld) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= arr:
                end, server_id = heapq.heappop(busy)
                heapq.heappush(available, i + (server_id - i) % k)
            
            if available:
                assigned = heapq.heappop(available)
                server_id = assigned % k
                counts[server_id] += 1
                heapq.heappush(busy, (arr + ld, server_id))
                
        max_reqs = max(counts)
        return [i for i, c in enumerate(counts) if c == max_reqs]