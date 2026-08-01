class Solution {
    public int trap(int[] height) {
        int left = 0;
        int leftHeight = height[left];
        int right = height.length - 1;
        int rightHeight = height[right];
        int volume = 0;

        while (left < right) {
            if (leftHeight <= rightHeight) {
                left++;

                if (leftHeight >= height[left]) {
                    volume += (leftHeight - height[left]);
                } else {
                    leftHeight = height[left];
                }
            } else {
                right--;

                if (rightHeight >= height[right]) {
                    volume += (rightHeight - height[right]);
                } else {
                    rightHeight = height[right];
                }
            }
        }
        return volume;
    }
}
