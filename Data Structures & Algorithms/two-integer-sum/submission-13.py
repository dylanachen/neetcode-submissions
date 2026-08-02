class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
        
            if nums[i] in seen.keys():
                return [seen[nums[i]], i]
            
            diff = target - nums[i]
            seen[diff] = i
