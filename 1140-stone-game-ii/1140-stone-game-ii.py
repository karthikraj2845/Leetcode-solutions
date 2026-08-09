class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suf = [0]*(n+1)
        for i in range(n-1,-1,-1):
            suf[i] = suf[i+1] + piles[i]
        dp = [[-1] * (n + 1) for _ in range(n + 1)]    
        def solve(i,m):
            if i >= n:
                return 0
            if i + 2*m >= n:
                return suf[i]
            if dp[i][m] != -1:
                return dp[i][m]    
            ans = 0
            for x in range(1,2*m+1):
                ans = max(ans,suf[i] - solve(i+x,max(m,x)))  
            dp[i][m] = ans    
            return ans
        return solve(0,1)                 

        