class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alpha_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
        new_string_list = []
        for letter in s:
            try:
                if letter in alpha_set or letter.isdigit():
                    new_string_list.append(letter)
            except:
                pass
        s = ''.join(new_string_list)
        return s == s[::-1]
