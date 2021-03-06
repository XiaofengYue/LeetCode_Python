class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        j = 0
        for i in range(len(nums)):
            nums[j] = nums[i]
            j += 1
            if nums[i] == val:
                j -= 1
        return j
