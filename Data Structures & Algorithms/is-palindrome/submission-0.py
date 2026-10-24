class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for n in s:
            if n.isalnum():
                st += n
        st = st.lower()
        return st[:] == st[::-1]
