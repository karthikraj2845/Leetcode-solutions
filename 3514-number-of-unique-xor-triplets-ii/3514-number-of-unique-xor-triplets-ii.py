class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        vals = list(set(nums))
        MAX = 2048

        dp = [[False] * MAX for _ in range(4)]
        dp[0][0] = True

        for t in range(3):
            for x in range(MAX):
                if dp[t][x]:
                    for v in vals:
                        dp[t + 1][x ^ v] = True

        return sum(dp[3])
                          
        