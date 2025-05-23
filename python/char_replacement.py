class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        longest = 0
        maxCount = 0
        count = collections.Counter()

        l = 0

        for r, c in enumerate(s):
            count[c] += 1
            maxCount = max(maxCount, count[c])

            while maxCount + k < r - l + 1:
                count[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l +1)
        
        return longest