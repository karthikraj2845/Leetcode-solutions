class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        freq = {}
        max_ = 0
        n = len(wall)
        for i in range(n):
            cur = 0
            for j in range(len(wall[i]) - 1):
                cur += wall[i][j]
                freq[cur] = freq.get(cur,0) + 1
                max_ = max(max_,freq[cur]) 
        print(max_)
        return n - max_
        