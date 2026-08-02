class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            diff = target - nums[i]
        
            if nums[i] in seen.keys():
                return [seen[nums[i]], i]
            
            seen[diff] = i
