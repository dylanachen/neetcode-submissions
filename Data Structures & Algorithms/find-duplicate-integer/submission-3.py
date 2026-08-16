class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # fast and slow pointers using n as the index to travel to
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        second_slow = 0
        while True:
            second_slow = nums[second_slow]
            slow = nums[slow]

            if slow == second_slow:
                return slow