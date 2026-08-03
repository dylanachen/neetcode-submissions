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
                l += 1
                l_height = max(l_height, height[l])
                area += l_height - height[l]
                
            else:
                r -= 1
                r_height = max(r_height, height[r])
                area += r_height - height[r]
        
        return area