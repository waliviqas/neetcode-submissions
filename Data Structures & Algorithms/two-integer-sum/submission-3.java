class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap <Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int saved = target - nums[i];

            if (map.containsKey(saved)) {
                return new int[] {map.getOrDefault(saved, -1), i};
            }

            map.put(nums[i], i);
        }

        return new int[] {};
    }
}
