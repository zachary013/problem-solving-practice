class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        prev_index = 0

        for i in range(0, len(nums)):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[prev_index]
                nums[prev_index] = temp
                prev_index += 1
        print(nums)
        