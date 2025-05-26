from math import log2, ceil

class BinaryLifting:
    def __init__(self, n):
        self.n = n
        self.log = ceil(log2(n)) + 1
        self.adj = [[] for _ in range(n)]
        self.depth = [0]*n
        self.parent = [[-1]*self.log for _ in range(n)]
    
    def add_edge(self, u ,v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    
    def dfs(self, node, par):
        self.parent[node][0] = par
        for i in range(1,self.log):
            if self.parent[node][i-1] != -1:
                self.parent[node][i] = self.parent[self.parent[node][i-1]][i-1]
        
        for child in self.adj[node]:
            if child != par:
                self.depth[child] = self.depth[node] + 1
                self.dfs(child,node)
        
    
    def build_ancestors(self, root = 0):
        self.dfs(root, -1)
    
    def lift_up(self, node, k):
        for i in range(self.log):
            if k & (1<<i):
                node = self.parent[node][i]
        
        return node
    
    def lca(self,u,v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        
        u = self.lift_up(u, self.depth[u] - self.depth[v])

        if u == v:
            return u
        
        for i in reversed(range(self.log)):
            if self.parent[u][i] != self.parent[v][i]:
                u = self.parent[u][i]
                v = self.parent[v][i]
        
        return self.parent[u][0]

    def dist(self,u,v):
        return self.depth[u] + self.depth[v] - 2 * self.depth[self.lca(u, v)]

