class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # traverse left to right keeping track of max_area
        # keep a current rectangle left bound pointer
        # the min of the bars in the considered window will be the height
        # only move the left pointer if the area found is >= max_area

        # problems: how do you consider the start of a new rectangle?

        # stack of (index, height) while traversing across (monotonically increasing height)
        bars = []
        max_area = float('-inf')

        for i, height in enumerate(heights):
            left_index = i
            while bars and height < bars[-1][1]:
                left_index, left_height = bars.pop()
                area = (i - left_index) * left_height
                max_area = max(max_area, area)

            bars.append([left_index, height])
            # print(bars)
        
        for i, height in bars[::-1]:
            area = (len(heights) - i) * height
            # print(area)
            max_area = max(max_area, area)
        
        return max_area