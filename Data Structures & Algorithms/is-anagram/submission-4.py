class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # empty array alphabet

        # for loop going through s 
        #     update letter in alphabet increment
        # for loop going through t
        #     update letter in alphabet decrement
        # if all array vals are 0
        #     return True 
        # else:
        #     return false


        alphabet = [0] * 26

        for i in range(len(s)):
            alphabet[ord(s[i]) - ord('a')]+=1
        for i in range(len(t)):
            alphabet[ord(t[i]) - ord('a')]-=1
        if all(x == 0 for x in alphabet):
            return True
        else:
            return False
