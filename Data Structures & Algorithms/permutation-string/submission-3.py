from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counts = defaultdict(int)
        window_counts = defaultdict(int)
        for i in range(len(s1)):
            s1_counts[s1[i]] += 1
            window_counts[s2[i]] += 1
        
        if window_counts == s1_counts:
            return True
            
        for i in range(len(s2) - len(s1)):
            window_counts[s2[i]] -= 1
            if window_counts[s2[i]] == 0:
                window_counts.pop(s2[i])

            window_counts[s2[i + len(s1)]] += 1

            if window_counts == s1_counts:
                return True
        
        return False