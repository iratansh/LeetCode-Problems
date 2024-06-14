class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1 or s == s[::-1]:
            return s

        res = ""
        for i in range(len(s)):
            p = 0
            while i - p >= 0 and i + p < len(s) and s[i - p ] == s[i + p]:
                if 2*p + 1 > len(res):
                    res = s[i - p: i + p + 1]
                p += 1    
            l, r = i, i + 1
            while r < len(s) and l >= 0 and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r + 1]
                l -= 1
                r += 1
        return res
