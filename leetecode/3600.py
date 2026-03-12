from typing import List

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.rank[pa] < self.rank[pb]:
            pa, pb = pb, pa
        self.parent[pb] = pa
        if self.rank[pa] == self.rank[pb]:
            self.rank[pa] += 1
        return True


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        
        def can(x):
            dsu = DSU(n)
            upgrades = 0
            used = 0
            
            optional = []
            
            # mandatory edges
            for u,v,s,m in edges:
                if m == 1:
                    if s < x:
                        return False
                    if not dsu.union(u,v):
                        return False
                    used += 1
                else:
                    optional.append((u,v,s))
            
            direct = []
            upgrade = []
            
            for u,v,s in optional:
                if s >= x:
                    direct.append((u,v))
                elif s*2 >= x:
                    upgrade.append((u,v))
            
            # use direct edges
            for u,v in direct:
                if dsu.union(u,v):
                    used += 1
            
            # use upgraded edges
            for u,v in upgrade:
                if used == n-1:
                    break
                if dsu.union(u,v):
                    upgrades += 1
                    used += 1
            
            return used == n-1 and upgrades <= k
        
        lo, hi = 1, max(e[2] for e in edges)*2
        ans = -1
        
        while lo <= hi:
            mid = (lo + hi)//2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans