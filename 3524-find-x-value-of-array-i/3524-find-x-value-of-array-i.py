class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k
        for x in nums:
            new_dp = [0] * k
            for r in range(k):
                new_r = (r * (x % k)) % k
                new_dp[new_r] += dp[r]
            new_dp[x % k] += 1    
            for r in range(k):
                ans[r] += new_dp[r]
            dp = new_dp
        return ans        

        