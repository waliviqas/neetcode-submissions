class Solution {
    public boolean hasDuplicate(int[] nums) {

        // for i = 0 ; i < nums.length ; i ++
        //     for j = i + 1 ; j < nums.length ; j++
        //         if i == j
        //             return true 

        // return false 

        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                return true;
            }

            map.put(nums[i], i);
        }

        return false;

        
    }
}