class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            if heights[l] <= heights[r]:
                area = (r - l) * heights[l]
                max_area = max(max_area, area)
                l += 1
            elif heights[l] > heights[r]:
                area = (r - l) * heights[r]
                max_area = max(max_area, area)
                r -= 1

        return max_area