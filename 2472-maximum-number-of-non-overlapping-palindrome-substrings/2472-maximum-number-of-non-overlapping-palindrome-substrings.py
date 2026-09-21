class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True
        dp = [0]*(n + 1)
        for i in range(n-1,-1,-1):
            skip = dp[i + 1]
            take = 0
            for j in range(n - 1,k + i -2, -1):
                if pal[i][j]:
                    take = max(take,1 + dp[j + 1])
            dp[i] = max(skip,take)
        return dp[0]            
                        

        