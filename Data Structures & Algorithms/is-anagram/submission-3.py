class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # alphaArray = 26 

        # for loop through s:
        #     alphaArray[letter i - a] + 1
        # for loop through t:
        #     alphaArray[letter i - a] - 1
        
        # if all array is 0:
        #     return True 
        # else: 
        #     reutrn False

        alpha = [0] * 26

        for i in range(len(s)):
            alpha[ord(s[i]) - ord('a')] += 1
        for i in range(len(t)):
            alpha[ord(t[i]) - ord('a')] -= 1
        if alpha == [0] * 26:
            return True 
        else:
            return False



        
