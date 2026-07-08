class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        digits = []
        positions = []   
        idx_map = {}
        for i, ch in enumerate(s):
            if ch != '0':
                idx_map[i] = len(digits)
                digits.append(int(ch))
                positions.append(i) 
        k = len(digits)
        prefix_sum = [0] * (k + 1)
        for i in range(k):
            prefix_sum[i + 1] = prefix_sum[i] + digits[i]
        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
        prefix_num = [0] * (k + 1)
        for i in range(k):
            prefix_num[i + 1] = (prefix_num[i] * 10 + digits[i]) % MOD
        # nextNonZero[i] = compressed index of first non-zero >= i
        nextNonZero = [-1] * n
        ptr = 0
        for i in range(n):
            while ptr < k and positions[ptr] < i:
                ptr += 1
            if ptr < k:
                nextNonZero[i] = ptr

        # prevNonZero[i] = compressed index of last non-zero <= i
        prevNonZero = [-1] * n
        ptr = k - 1
        for i in range(n - 1, -1, -1):
            while ptr >= 0 and positions[ptr] > i:
                ptr -= 1
            if ptr >= 0:
                prevNonZero[i] = ptr
        ans = []

        for l, r in queries:
            left = nextNonZero[l]
            right = prevNonZero[r]

            if left == -1 or right == -1 or left > right:
                ans.append(0)
                continue

            length = right - left + 1

            # Extract concatenated number
            x = (
                prefix_num[right + 1]
                - prefix_num[left] * pow10[length]
            ) % MOD

            # Sum of digits
            digit_sum = prefix_sum[right + 1] - prefix_sum[left]

            ans.append((x * digit_sum) % MOD)

        return ans            
             
        