class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            res = max(res, r - l + 1)
        
        return res


        # "abcb"
        # r = 0, l = 0:
        # while a in seen x

        # seen.append(a)
        # res = max(0, 1) = 1

        # r = 1, l = 0
        # while b in seen x

        # seen.append(b)
        # res = max(1, 2) = 2

        # r = 2, l = 0:
        # while c in seen x

        # seen.append(c)
        # res = max(2, 3) = 3

        # r = 3, l = 0:
        # while b in seen yes 
        # seen.remove(a)
        # l = 1
        # seen.remove(b)
        # l = 2

        # seen.append(b)
        # res = max(3, 3 -2 + 1 = 2) = 3

        # answer: 3
