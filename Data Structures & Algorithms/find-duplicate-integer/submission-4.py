class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # fast and slow pointers using n as the index to travel to
        # once our pointers intercept, we are now the same distance to the duplicated number (in our cycle) as we would be from index 0
        # set off a second slow pointer and once both slow pointers intercept, we are at the duplicated number
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