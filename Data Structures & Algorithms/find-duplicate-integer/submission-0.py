class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # brute force solution is to create a hashmap of seen nums and compare each new node against the existing, returning upon repeat
        seen = set()

        for num in nums:
            if num in seen:
                return num

            seen.add(num)
            