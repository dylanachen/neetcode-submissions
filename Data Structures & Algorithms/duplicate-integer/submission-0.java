class Solution {
    public boolean hasDuplicate(int[] nums) {
        ArrayList<Integer> seen = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (seen.contains(nums[i])) {
                return true;
            } else {
                seen.add(nums[i]);
            }
        }
        return false;
    }
}
