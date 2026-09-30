class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = {0, 0};
        HashMap<Integer, Integer> diffs = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            Integer difference = target - nums[i];

            if (diffs.containsKey(difference)) {
                res[0] = diffs.get(difference);
                res[1] = i;
                break;
            }
            else {
                diffs.put(nums[i], i);
            }
        }
        return res;
    }
}
