class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        n = len(word)
        considered = 0
        n_press = 1
        while n > 0:
            if n <= 8:
                ans += n_press*n
                return ans
            else:
                ans += n_press*8
                n_press += 1
                n -= 8
                   
        return ans    
