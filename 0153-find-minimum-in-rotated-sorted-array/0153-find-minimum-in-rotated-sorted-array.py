class Solution:
    def findMin(self, nums: List[int]) -> int:
        high = len(nums)-1
        low = 0
        while high > low:
            mid = (high+low)//2
            if nums[mid] < nums[high]:
                high = mid
            elif nums[mid] > nums[high]:
                low = mid+1
        return nums[high]  



                   
