class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        cnt = [0] * 10
        for x in digits:
            cnt[x] += 1
        ans = 0
        for last in range(0, 10, 2):
            if cnt[last] == 0:
                continue
            cnt[last] -= 1
            for first in range(1, 10):
                if cnt[first] == 0:
                   continue
                cnt[first] -= 1
                for mid in range(10):
                    if cnt[mid] == 0:continue
                    ans += 1
                cnt[first] += 1
            cnt[last] += 1
        return ans
