class Solution:
    def isPalindrome(self, s: str) -> bool:
        # left pointer 
        # right pointer

        # while loop going through arr 
        #     if left pointer is a space or not alpha num
        #         increment left 
        #     if right pointer is space or not alpha num
        #         decrement right 
        #     if left pointer != right pointer 
        #         return false 
        # return true

        l = 0
        r = len(s) - 1
    
        l, r = 0, len(s) - 1

        while l < r:

            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        
        return True
            
        
        