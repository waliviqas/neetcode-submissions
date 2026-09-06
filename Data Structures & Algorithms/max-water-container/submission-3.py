class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # - start with i 
        # - check against every other idx 
        # - note down the largest one from that iteration (compare to current longest holder)


        # left pointer 
        # right pointer 
        # while loop going through height 
        #     width = r - l
        #     height = min of val @ left, val @ right 
        #     area = width * height 

        #     maximum = max of area, maximum 

        #     if height of left < height of right 
        #         increment left 
        #     elif of height of right > height of left 
        #         decrement right 
        #     increment left 
        #     decrement right


        l, r = 0, len(heights) - 1
        maximum = 0
        while l < r:
            width = r - l
            length = min(heights[l], heights[r])
            area = width * length 

            maximum = max(area, maximum)

            if heights[l] < heights[r]:
                l+=1
            elif heights[l] > heights[r]:
                r-=1
            else:
                l+=1
                r-=1
        return maximum
            