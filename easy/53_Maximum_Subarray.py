class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_Sum = 0
        max_Sum = 0
        for num in nums:
            if temp_Sum + num > 0:
                temp_Sum += num
                max_Sum = max(max_Sum, temp_Sum)
            else:
                temp_Sum = 0
        if max(nums) < 0:
            return max(nums)
        return max_Sum


# 大神的easy way
# for i in range(1, len(nums)):
#         if nums[i-1] > 0:
#             nums[i] += nums[i-1]
#     return max(nums)
