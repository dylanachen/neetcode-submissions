from collections import defaultdict
from operator import itemgetter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force
        # count map(num: count)
        # sort map by counts descending
        # return first k values of the sorted count map

        num_counts = defaultdict(int)

        for num in nums:
            num_counts[num] += 1
        
        nums_sorted_by_count_desc = dict(sorted(
            num_counts.items(), 
            key=itemgetter(1), 
            reverse=True
        ))
        
        result = []
        for key, value in nums_sorted_by_count_desc.items():
            result.append(key)
        
        return result[:k]