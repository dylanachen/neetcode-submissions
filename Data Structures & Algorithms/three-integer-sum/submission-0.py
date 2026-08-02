class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort and then use pointers
        nums.sort()

        res = []

        for l in range(len(nums)):
            # if the base number in the set is already >0
            if nums[l] > 0:
                break
            
            # if l is past the first num, but equals the previous num, increment it
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            
            # m and r pointers to find the sums within the space between l and the end of nums
            m = l + 1
            r = len(nums) - 1
            while m < r:
                three_sum = nums[l] + nums[m] + nums[r]
                
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    m += 1
                else:
                    res.append([nums[l], nums[m], nums[r]])
                    m += 1
                    r -= 1
                    while nums[m] == nums[m - 1] and m < r:
                        m += 1

        return res