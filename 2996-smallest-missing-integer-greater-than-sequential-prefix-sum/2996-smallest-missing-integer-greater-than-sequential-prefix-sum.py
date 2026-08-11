class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        num_set = set(nums)
        n = len(nums)
        pre_sum = nums[0]
        for i in range(1,n):
            if nums[i] == nums[i-1] + 1:
                pre_sum += nums[i]
            else:
                break
        while pre_sum in num_set:
            pre_sum += 1
        return pre_sum               


        