class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n = len(nums)
        seen = set()
        cur_sum = nums[0]
        for i in range(1,n):
            cur_sum += nums[i] 
            if cur_sum in seen:return True
            seen.add(cur_sum)
            cur_sum -= nums[i - 1]
        return False    
        