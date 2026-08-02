from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        hashmap = defaultdict(int)

        for num in nums:
            if not hashmap[num]:
                hashmap[num] = hashmap[num - 1] + hashmap[num + 1] + 1
                hashmap[num - hashmap[num - 1]] = hashmap[num]
                hashmap[num + hashmap[num + 1]] = hashmap[num]
                max_len = max(max_len, hashmap[num])
        
        return max_len