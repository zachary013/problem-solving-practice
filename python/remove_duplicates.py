#leetcode problem : remove duplicates from sorted array

class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return len(nums)
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        
        return j+1
        
#testing the class
nums = [1, 3, 3, 4, 5, 5, 6, 7, 8, 8]
result = Solution().removeDuplicates(nums)
print(result)