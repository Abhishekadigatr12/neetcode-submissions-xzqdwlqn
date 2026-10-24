class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j = 0,0
        r = []
        while i<len(word1) or j< len(word2):
            if i< len(word1):
                r.append(word1[i])
            if j<len(word2):
                r.append(word2[j])
            i+=1
            j+=1
        return "".join(r)