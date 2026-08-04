class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        t_counts = {}
        window_counts = {}

        for c in t:
            t_counts[c] = 1 + t_counts.get(c, 0)

        have = 0
        need = len(t_counts)

        result = [-1, -1]
        min_len = float('infinity')

        l = 0
        for r in range(len(s)):
            c = s[r]
            window_counts[c] = 1 + window_counts.get(c, 0)

            if c in t_counts and window_counts[c] == t_counts[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < min_len:
                    result = [l, r]
                    min_len = r - l + 1
                
                window_counts[s[l]] -= 1
                if s[l] in t_counts and window_counts[s[l]] < t_counts[s[l]]:
                    have -= 1
                l += 1
        
        l, r = result

        return s[l:r + 1] if min_len != float('infinity') else ""
