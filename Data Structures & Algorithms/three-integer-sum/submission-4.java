class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        List<List<Integer>> result = new ArrayList<>();

        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 2; i++) {

            if (i > 0 && nums[i] == nums[i-1]) {
                continue; //skips to the next iteration
            }

            int curr = nums[i];
            int left = i + 1;
            int right = nums.length - 1;

            while (left < right) {
                int l = nums[left];
                int r = nums[right];

                int target = -nums[i];

                if (l + r < target) {
                    left++;
                    continue;
                }

                if (l + r > target) {
                    right--;
                    continue;
                } 

                List<Integer> triplet = new ArrayList<>();
                triplet.add(l);
                triplet.add(r);
                triplet.add(nums[i]);
                result.add(triplet);

                left++;
                right--;

                while (left < right && nums[left] == nums[left-1]) {
                    left++;
                }

            }

            
        }

        return result;
        
    }
}
