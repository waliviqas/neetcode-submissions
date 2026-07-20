class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        
        List<List<Integer>> result = new ArrayList<>();

        // Step 1: sort the array from least to greatest
        // We will do two pointer first 
        Arrays.sort(nums); // .sort() method sorts it least to greatest

        // Step 2: Find the first number of the triplet
        // you stop at length - 2 because if you get to 
        // the second last one, you will not have enough 
        // for a pair after the one on i
        for (int i = 0; i < nums.length - 2; i++) {

            // telling it to skip duplicate values
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            // we need two numbers to the right of i 
            // that add up to the opposite of nums[i]
            // Example: if nums[i] is -4, we need a pair That sums up to 4.
            int target = -nums[i];

            // Step 4: set up the two pointers
            // left starts just after i, right starts at the end
            // now you are just doing two sum on the rest of the array
            int left = i + 1;
            int right = nums.length - 1;

            while (left < right) {
                int l = nums[left];
                int r = nums[right];
                int pairSum = l + r;

                if (pairSum < target) {
                    left++;
                    continue;
                }

                if (pairSum > target) {
                    right--;
                    continue;
                }

                // else the triplet is fully set 
                List<Integer> triplet = new ArrayList<>();
                triplet.add(nums[i]);
                triplet.add(nums[left]);
                triplet.add(nums[right]);
                result.add(triplet); // add the whole thing to the result

                left++;
                right--;

                // skip over duplicate left values for next iteration 
                while (left < right && nums[left] == nums[left - 1]) {
                    left++;
                }


            }
        }
        return result;
    }
}
