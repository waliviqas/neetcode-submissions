class Solution:
    def isPalindrome(self, s: str) -> bool:

        b = []
        d = []

        for i in range(len(s)):
            c = s[i].lower()
            if not c.isalnum():
                continue
            b.append(c)
        
        for i in range(len(s) - 1, -1, -1):
            e = s[i].lower()
            if not e.isalnum():
                continue
            d.append(e)
        
        if b != d:
            return False
        
        return True
                   