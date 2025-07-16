class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
    
    def find(self,i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        
        return self.parent[i]
    
    def union(self,u,v):
        find_u = self.find(u)
        find_v = self.find(v)
        if find_u == find_v:
            return False
        self.parent[find_u] = find_v
        return True
