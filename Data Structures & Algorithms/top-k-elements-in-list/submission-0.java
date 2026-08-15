class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        Map<Integer, Integer> count = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];

            if (count.containsKey(num)) {
                count.put(num, count.get(num) + 1);
            } else {
                count.put(num, 1);
            }
        }

        List<Integer>[] buckets = new List[nums.length + 1];
        for (int i = 0; i < buckets.length; i++) {
            buckets[i] = new ArrayList<>();
        }

        List<Integer> keys = new ArrayList<>(count.keySet());
        for (int i = 0; i < keys.size(); i++) {
            int num = keys.get(i);
            int freq = count.get(num);
            buckets[freq].add(num);
        }

        int[] res = new int[k];
        int idx = 0;
        for (int i = buckets.length - 1; i > 0; i--) {
            for (int j = 0; j < buckets[i].size(); j++) {
                res[idx] = buckets[i].get(j);
                idx++;
                if (idx == k){
                    return res;
                }
            }
        }
    return res;

    }
}
