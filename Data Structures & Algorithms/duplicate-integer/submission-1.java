
class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<Integer>();

        for (int i = 0; i < nums.length; i++) {
            Integer num = nums[i];

            if (seen.contains(num)) {
                return true;
            }
            seen.add(num);
        }
        return false;
    }
}