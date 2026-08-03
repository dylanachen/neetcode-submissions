class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        max_len = 0

        for r in range(len(s)):
            if s[r] in seen:
                l = max(l, seen[s[r]] + 1)
            
            seen[s[r]] = r
            max_len = max(max_len, r - l + 1)
        
        return max_len