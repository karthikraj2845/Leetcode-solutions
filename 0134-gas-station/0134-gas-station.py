class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        extra = []
        total = 0
        for i in range(n):
            cur = gas[i] - cost[i]
            extra.append(cur)
            total += cur
        if total < 0:return -1
        ans = 0
        cur = 0
        for i in range(n):
            cur += extra[i]
            if cur < 0:
                ans = i + 1
                cur = 0
        return ans       

        