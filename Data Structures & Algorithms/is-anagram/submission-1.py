class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = [0] * 26
        map_t = [0] * 26
        for c in s:
            map_s[ord(c)-ord('a')] += 1
        for c in t:
            map_t[ord(c)-ord('a')] += 1
        if map_s == map_t:
            return True
        else:
            return False