class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        l_height = height[l]
        r_height = height[r]
        area = 0

        while l < r:
            if height[l] <= height[r]:
                # if shorter than last tallest left bar, add difference in water vol
                # if taller, update last tallest left bar
                if height[l] < l_height:
                    area += l_height - height[l]
                else:
                    l_height = height[l]
                l += 1
            
            else:
                if height[r] < r_height:
                    area += r_height - height[r]
                else:
                    r_height = height[r]
                r -= 1
        
        return area