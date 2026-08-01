class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        leftHeight = height[left]
        right = len(height) - 1
        rightHeight = height[right]
        volume = 0

        while left < right:
            if leftHeight <= rightHeight:
                left += 1

                if leftHeight >= height[left]:
                    volume += (leftHeight - height[left])
                else:
                    leftHeight = height[left]
            else:
                right -= 1

                if rightHeight >= height[right]:
                    volume += (rightHeight - height[right])
                else:
                    rightHeight = height[right]
        
        return volume