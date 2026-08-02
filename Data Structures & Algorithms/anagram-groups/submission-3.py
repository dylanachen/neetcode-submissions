from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a defaultdict(unique character count maps: list of strs)
        # iterate through the strings
            # create a character count list = [0] * 26
            # iterate through each char in the string
                # use ord to find char index and += 1
            # tuple(characer count list) as index in defaultdict, appending the current string
        # return list of the values of the defaultdict

        result = defaultdict(list)

        for s in strs:
            char_counts = [0] * 26
            for c in s:
                c_idx = ord(c) - ord('a')
                char_counts[c_idx] += 1
            
            result[tuple(char_counts)].append(s)
        
        return list(result.values())