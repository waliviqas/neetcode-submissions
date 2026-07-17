class Solution {
    public int[] twoSum(int[] numbers, int target) {
    //     left = 0
    //     right = numbers.size - 1
    //     while left < right 
    //         l = numbers[left]
    //         r = numbers[right]
    //         if l + r < target
    //             left++
    //             continue
    //         if l + r > target
    //             right--
    //             continue
            
    //         return {left, right}
    // }
    // return {-1, -1}

    int left = 0;
    int right = numbers.length - 1;

    while (left < right) {
        int l = numbers[left];
        int r = numbers[right];

        if (l + r < target) {
            left++;
            continue;
        }

        if (l + r > target) {
            right--;
            continue;
        }

        return new int[] {left + 1, right + 1};
    }

    return new int[] {-1, -1};
}
}
