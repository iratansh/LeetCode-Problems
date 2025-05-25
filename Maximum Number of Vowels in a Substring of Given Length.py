class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        maxLen = 0

        for i in range(k): # find the num of vowels in the first substring of len = k
            if s[i] in vowels:
                maxLen += 1
        numVowels = maxLen
        for r in range(k, len(s)):
            # remove the first element in the substring if it is a vowel
            if s[r - k] in vowels:
                numVowels -= 1
            if s[r] in vowels:
                numVowels += 1
            maxLen = max(maxLen, numVowels)
        return maxLen
