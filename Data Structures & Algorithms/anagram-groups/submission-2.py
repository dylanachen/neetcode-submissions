from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create anagram_map(count_map: index in list) and anagram_list
        # iterate through each string to:
            # find it's count map
            # check if the count map exists in the anagram_map
            # if it does, append the string to the sublist at the appropriate index
            # if it does not, create a new entry in the overall list and in the anagram_map with the current string

        anagram_map = defaultdict(int)
        result = []

        for s in strs:
            str_counts = defaultdict(int)
            for char in s:
                str_counts[char] += 1

            str_counts = frozenset(str_counts.items())

            if str_counts in anagram_map.keys():
                result[anagram_map[str_counts]].append(s)
            else:
                result.append([s])
                anagram_map[str_counts] = len(result) - 1
        
        return result
