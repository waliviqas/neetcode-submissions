class Solution {
    public int maxArea(int[] heights) {
        // Step 1: Set up the two pointers
        int left = 0;
        int right = heights.length - 1;

        // Step 2: Track the best area found so far
        int max = 0;

        // Step 3: sweep the pointers towards each other 
        while (left < right) {

            // width = distance between the two walls
            int width = right - left;

            //water is capped by the shorter wall 
            // anything above it spills over
            int shorter = Math.min(heights[left], heights[right]);

            int area = width * shorter;

            // step 4: record if it beats the best one so far
            if (area > max) {
                max = area;
            }

            // step 5: whichever side has the shorter wall moves in one
            // max keeps updating until the end and recalculating
            // and keeps the largest value every time
            // always move the shorter wall
            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }

        return max;
    }
}
