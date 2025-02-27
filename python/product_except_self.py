class Solution(object):
    def productExceptSelf(self, nums):
        
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in reversed(range(n - 1)):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        return [ prefix[i] * postfix[i] for i in range(n)]

         