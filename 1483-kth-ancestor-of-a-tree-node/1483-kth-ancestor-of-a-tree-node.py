class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.n = n
        self.parent = parent
        self.cols = n.bit_length()
        self.ancestor = [[-1]*self.cols for _ in range(n)]
        for j in range(self.cols):
            for i in range(n):
                if j == 0:self.ancestor[i][j] = parent[i]
                else:
                    prev = self.ancestor[i][j - 1]
                    if prev != -1:
                        self.ancestor[i][j] = self.ancestor[prev][j - 1]
                    
    def getKthAncestor(self, node: int, k: int) -> int:
        ans = node 
        LOG = k.bit_length()
        for j in range(LOG):
            if (k & (1 << j)):ans = self.ancestor[ans][j]
            if ans == -1:return -1
        return ans    
        
        


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)