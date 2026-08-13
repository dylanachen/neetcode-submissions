class Solution:
    def findMin(self, nums: List[int]) -> int:
        # finding the min element of the array means comparing r and l
        # if nums[r] > nums[m], min is in the left half
        # otherwise, it is in the right half

        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + ((r - l) // 2)
            
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        return nums[l]