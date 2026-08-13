class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # double binary search method
        # first binary search finds the point at which it splits into two sorted arrays
        # then we perform a second binary search on the appropriate half to then locate if the target is present
        
        l = 0
        r = len(nums) - 1

        # binary search for minimum
        while l < r:
            m = l + ((r - l) // 2)

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = l
        l, r = 0, len(nums) - 1

        # binary search for target in correct sorted half
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
            # r = len(nums) - 1
        else:
            # l = 0
            r = pivot - 1
            
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1