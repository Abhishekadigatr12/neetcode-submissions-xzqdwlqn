class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        i = 0 
        j = l-1
        while i<j:
            while i<j and not s[i].isalnum():
                i+=1
            while j>i and not s[j].isalnum():
                j-=1
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        return True