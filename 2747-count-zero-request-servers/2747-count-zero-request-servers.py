class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda item: item[1])
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        
        res = [0] * len(queries)
        counts = [0] * (n + 1)
        active_servers = 0
        
        left = 0
        right = 0
        
        for q_time, q_idx in sorted_queries:
            while right < len(logs) and logs[right][1] <= q_time:
                server_id = logs[right][0]
                if counts[server_id] == 0:
                    active_servers += 1
                counts[server_id] += 1
                right += 1
                
            while left < len(logs) and logs[left][1] < q_time - x:
                server_id = logs[left][0]
                counts[server_id] -= 1
                if counts[server_id] == 0:
                    active_servers -= 1
                left += 1
                
            res[q_idx] = n - active_servers
            
        return res