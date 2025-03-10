class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1
            if freq[char] % 2 == 0:
                count -= 1
            else:
                count += 1
            
        if count > 1:
            return len(s) - count + 1
        return len(s)
