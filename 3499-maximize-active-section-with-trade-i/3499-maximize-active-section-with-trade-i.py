class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        original = s.count('1')
        t = '1' + s + '1'
        runs = []
        i = 0
        while i < len(t):
            j = i
            while j < len(t) and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j

        max_gain = 0
        for i in range(1, len(runs) - 1):
            if runs[i][0] == '1' and runs[i - 1][0] == '0' and runs[i + 1][0] == '0':
                left_zero = runs[i - 1][1]
                right_zero = runs[i + 1][1]
                max_gain = max(
                    max_gain,
                    left_zero + right_zero
                )

        return min(n, original + max_gain)        