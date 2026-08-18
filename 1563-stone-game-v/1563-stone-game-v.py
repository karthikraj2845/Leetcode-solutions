class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        dp = [[-1]*(n+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][i] = 0
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
        def helper(l,r):
            if dp[l][r] != -1:return dp[l][r]
            cur_sum = prefix[r+1] - prefix[l]
            cur_len = r - l + 1
            ans = 0
            for b in range(cur_len):
                l_row = prefix[l+b+1] - prefix[l]
                r_row = cur_sum - l_row
                if l_row > r_row:
                    cur = r_row + helper(l+b+1,r)
                elif l_row < r_row:
                    cur = l_row + helper(l,l+b)
                else:
                    take_left = l_row + helper(l,l+b) 
                    take_right = r_row + helper(l+b+1,r)
                    cur = max(take_left,take_right)
                ans = max(ans,cur)
            dp[l][r] = ans    
            return ans
        return helper(0,n-1)                   
        