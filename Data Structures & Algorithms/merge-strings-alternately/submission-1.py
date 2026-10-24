class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        r = []
        for i in range(max(n,m)):
            if i<n:
                r.append(word1[i])
            if i<m:
                r.append(word2[i])
        return "".join(r)