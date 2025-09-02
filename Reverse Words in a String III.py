class Solution:
    def reverseWords(self, s: str) -> str:
        # the idea to not to reverse the entire string - but to reverse each word in the string. 
        # Reverse the input string while maintaining the original order of words
        # two-pointer approach? Start the left point at the start of the word and then keep the right pointer at the end of the word and swap each character in the left and right pointers? while moving l, r forwards and backwards respectively till they have the same value -> then move to the next word?
        # you can define the end of a word as if its next char is whitespace or if r + 1 == len(s)?
        chars = list(s)
        l, r = 0, 0
        while r < len(s) and s[r] != " ": # move r to the end of the word
            r += 1
        
        def reverse(l, r):
            while l < r:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1
        
        start = 0
        for i in range(len(chars) + 1):
            if i == len(chars) or chars[i] == " ":
                reverse(start, i - 1)
                start = i + 1

        return "".join(chars)
