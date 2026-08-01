class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0]* (n+1) for _ in range(n + 1)]
        for i in range(n):
            dp[i][i] = nums[i]
        for length in range(2,n+1):
            for l in range(n - length + 1):
                r = l + length - 1
                take_l = nums[l] - dp[l+1][r]
                take_r = nums[r] - dp[l][r - 1]
                dp[l][r] = max(take_l,take_r)
        return dp[0][n - 1] >= 0        
                


        