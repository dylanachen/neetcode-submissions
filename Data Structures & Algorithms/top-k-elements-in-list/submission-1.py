from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        # get count map(nums: counts)
        # iterate over count map
        # len(nums)+1 list of lists with the index being the freq and sublists containing nums with that freq
        # reverse iterate over freq map until result list is len == k
        counts = defaultdict(int)
        freqs = [[] for i in range(len(nums) + 1)]

        for num in nums:
            counts[num] += 1
        
        for num, count in counts.items():
            freqs[count].append(num)
        
        result = []
        for i in range(len(freqs) - 1, 0, -1):
            for num in freqs[i]:
                result.append(num)
                if len(result) == k:
                    return result