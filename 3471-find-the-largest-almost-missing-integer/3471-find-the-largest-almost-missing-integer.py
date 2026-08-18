class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq= {}
        n = len(nums)
        max_ = float('-inf')
        for num in nums:
            freq[num] = freq.get(num,0) + 1
            max_ = max(max_,num)
        ans = -1    
        if k == 1:
            for num,f in freq.items():
                if f == 1:ans = max(ans,num)
        elif k == n:
            ans = max_
        else:
            if freq[nums[0]] == 1:
                ans = nums[0]
            if freq[nums[-1]] == 1:
                ans = max(ans,nums[-1])
        return ans                           
            

        