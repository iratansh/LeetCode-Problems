class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        charToWord = {} # key = pattern, val = corresponding word
        wordToChar = {} # key = corresponding word, val = pattern
        sList = s.split()

        if len(pattern) != len(sList):
            return False

        for i in range(len(pattern)):
            c = pattern[i]
            w = sList[i]

            if c not in charToWord:
                charToWord[c] = w
            if w not in wordToChar:
                wordToChar[w] = c
            if charToWord[c] != w or wordToChar[w] != c:
                return False
        return True
