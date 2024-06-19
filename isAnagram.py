class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for el in s:
            s_dict[el] = 0
        for el in t:
            t_dict[el] = 0
        for el in s:
            s_dict[el] += 1
        for el in t:
            t_dict[el] += 1
        s_dict = dict(sorted(s_dict.items()))
        t_dict = dict(sorted(t_dict.items()))
        return s_dict == t_dict
