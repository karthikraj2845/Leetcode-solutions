class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        i = 0
        j = 0
        cur_sum = 0
        ans = float('inf')
        bestMin = float('inf')
        min_len = [float('inf')]*n
        while (j < n):
            cur_sum += arr[j]
            while cur_sum > target:
                cur_sum -= arr[i]
                i += 1
            if cur_sum == target:
                cur_len = j - i + 1
                if (i > 0 and min_len[i - 1] != float('inf')): 
                    prev_min = min_len[i - 1]
                    ans = min(ans,cur_len + prev_min)
                bestMin = min(bestMin,cur_len)
            min_len[j] = bestMin
            j += 1
        return -1 if ans == float('inf') else ans            

        