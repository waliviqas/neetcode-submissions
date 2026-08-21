class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # every time the window - the max frequency is greater than K, that means there are too many chars to replace
        # in that case move to the next char 

        maxf = 0 
        count = 0
        l = 0
        count = {}
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


        # X:0, Y:2

        # r = 0, l = 0
        # count[X] = 1 + 0 = 1
        # maxf = max(0, 1) = 1
        # while (0-0+1) - 0 > 2 = 1 > 2 x
        # res = 0, 1 = 1

        # r = 1, l = 0 
        # count[Y] = 1 + 0
        # maxf = 1,1 = 1
        # while (1-0+1) > 2 = 2 > 2 x
        # res = 1, 2 = 2

        # r = 2, l = 0
        # count[Y] = 1 + 1
        # maxf = 1, 2 = 2
        # while 2-0+1 - 2 > 2 = 1 > 2 x
        
        # res = 2, 3 = 3

        # r = 3, l = 0
        # count[X] = 1
        # maxf = 2, 1 = 2
        # while(3-0+1) - 2 > 2 = 2 > 2 x
        # res = 3, 4 = 4
