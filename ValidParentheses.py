class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 0:
            characters_dict = {'(':')', '[':']', '{':'}'}
            for i in range(len(s) - 1):
                if characters_dict[s[i]] == s[i + 1]:
                    return True
        return False
