class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n + 1)
        MOD = 10**9 + 7
        dp[0] = 1
        last = [-1]*26
        for i in range(1,n + 1):
            dp[i] = (2*dp[i - 1]) % MOD
            idx = ord(s[i - 1]) - ord('a')
            if last[idx] != -1:
                dp[i] = dp[i] - dp[last[idx]] + MOD
                dp[i] %= MOD
            last[idx] = i - 1
        return (dp[n] - 1 + MOD) % MOD  
        