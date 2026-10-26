class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    current_sum = grid[i][j] % k
                    grid[i][j] = 0 
                    
                    stack = [(i, j)]
                    while stack:
                        r, c = stack.pop()
                        
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = r + dr, c + dc
                            
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                current_sum = (current_sum + grid[nr][nc]) % k
                                grid[nr][nc] = 0 
                                stack.append((nr, nc))
                                
                    if current_sum == 0:
                        count += 1
                        
        return count