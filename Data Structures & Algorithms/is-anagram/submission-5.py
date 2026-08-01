from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = defaultdict(int)
        t_chars = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            s_chars[s[i]] += 1
            t_chars[t[i]] += 1

        if s_chars == t_chars:
            return True
        
        return False