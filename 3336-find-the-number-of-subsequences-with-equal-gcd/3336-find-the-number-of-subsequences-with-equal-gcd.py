from typing import List
from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        MAX = 200
        dp = [[0] * (MAX + 1) for _ in range(MAX + 1)]
        dp[0][0] = 1
        for x in nums:
            new_dp = [[0] * (MAX + 1) for _ in range(MAX + 1)]
            for g1 in range(MAX + 1):
                for g2 in range(MAX + 1):
                    ways = dp[g1][g2]
                    if ways == 0:
                        continue
                    # 1. Ignore x
                    new_dp[g1][g2] = (
                        new_dp[g1][g2] + ways
                    ) % MOD
                    # 2. Put x in seq1
                    ng1 = gcd(g1, x)
                    new_dp[ng1][g2] = (
                        new_dp[ng1][g2] + ways
                    ) % MOD
                    # 3. Put x in seq2
                    ng2 = gcd(g2, x)
                    new_dp[g1][ng2] = (
                        new_dp[g1][ng2] + ways
                    ) % MOD
            dp = new_dp
        ans = 0
        for g in range(1, MAX + 1):
            ans = (ans + dp[g][g]) % MOD
        return ans