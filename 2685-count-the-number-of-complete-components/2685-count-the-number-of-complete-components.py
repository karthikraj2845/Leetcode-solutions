class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        vis = [0]*n
        def dfs(mat,node,v,component):
            component.append(node)
            v[node] = 1
            for nei in mat[node]:
                if v[nei] != 1:
                    dfs(mat,nei,v,component)        
        def is_complete_component(component, mat):
            nc = len(component)
            for node in component:
                if len(mat[node]) != nc - 1: 
                    return False
            return True            
        ans = 0
        for i in range(n):
            if vis[i] == 0:
                c = []
                dfs(adj,i,vis,c)
                if is_complete_component(c,adj):
                    ans += 1
        return ans            
                        

        