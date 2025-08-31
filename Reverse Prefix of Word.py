class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        r = 0
        rev_str = ""
        if ch not in word:
            return word

        while r < len(word):
            if word[r] == ch:
                rev_str += ch
                r += 1
                break
            rev_str += word[r]
            r += 1
        return rev_str[::-1] + word[r::] 
