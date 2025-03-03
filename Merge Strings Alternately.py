class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1_left, w2_left = 0, 0  
        res = []

        while w1_left < len(word1) and w2_left < len(word2):
            res.append(word1[w1_left])
            res.append(word2[w2_left])
            w1_left += 1
            w2_left += 1

        res.append(word1[w1_left:])
        res.append(word2[w2_left:])  

        return ''.join(res)
