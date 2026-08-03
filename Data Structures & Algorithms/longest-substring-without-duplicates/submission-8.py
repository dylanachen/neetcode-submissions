class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        l = 0
        r = 1
        max_len = 1
        char_set = set(s[l])

        while r < len(s):
            if s[r] not in char_set:
                max_len = max(max_len, r - l + 1)
                char_set.add(s[r])
                r += 1
            else:
                while s[l] != s[r]:
                    l += 1
                l += 1
                char_set = set(s[l:r])
                # l = r - 1
        
        return max_len