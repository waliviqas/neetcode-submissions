class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        maxf = 0
        l = 0
        res = 0

        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res


# A:2, B:1, C:1

# r = 0
# count[A] = 1
# maxf = 1
# res = 1

# r = 1
# count[A] = 2
# maxf = 2
# win length = 2
# res = 2

# r = 2
# count[B] = 1
# maxf = 2,1 = 2
# win length = 2
# res = 2,2 = 2

# r = 3
# count[A] = 3
# maxf = 2, 3 = 3
# win length = 4
# res = 2, 4 = 4

# r = 4
# count[C] = 1
# maxf = 3, 1 = 3
# win length = 4-0 + 1 = 5
# 5 - 3 = 2 > 1 yes
# l = 1
# res = 4, 4
