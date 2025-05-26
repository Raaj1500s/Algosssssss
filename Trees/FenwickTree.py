class FenwickTree:
    def __init__(self,n):
        self.size = [0]*(n+1)
    
    def query(self,i):
        res = 0
        while i > 0:
            res += self.size[i]
            i -= i & -i
        
        return res
    
    def update(self,i,val):
        if i <= 0:
            return
        while i < len(self.size):
            self.size[i] += val
            i += i & -i
