class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        l = 0
        longest = 0
        n = len(s)
        substring = set()

        for r in range(n):
            #Not Valid
            while s[r] in substring:
                substring.remove(s[l])
                l = l + 1
            #Valid
            w = r - l + 1
            longest = max(longest, w)
            substring.add(s[r])

        return longest
        