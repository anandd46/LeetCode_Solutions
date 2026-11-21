class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        new_parent = list(parent)
        last_seen = [-1] * 26
        stack = [(0, -1)]
        
        while stack:
            u, prev = stack.pop()
            if u >= 0:
                c = ord(s[u]) - 97
                old = last_seen[c]
                if u != 0 and old != -1:
                    new_parent[u] = old
                last_seen[c] = u
                stack.append((~u, old))
                for v in adj[u]:
                    stack.append((v, -1))
            else:
                u = ~u
                last_seen[ord(s[u]) - 97] = prev
                
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        order = [0]
        for u in order:
            order.extend(new_adj[u])
            
        ans = [1] * n
        for u in reversed(order):
            p = new_parent[u]
            if p != -1:
                ans[p] += ans[u]
                
        return ans