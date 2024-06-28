class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        elif t == s:
            return t

        haveDict, needDict = defaultdict(int), defaultdict(int)
        for el in t:
            haveDict[el] = 1 + haveDict.get(el, 0)
        have, need = 0, len(haveDict)
        ans, ansLength = [-1, -1], float("infinity") 
        l_pointer = 0

        for r_pointer in range(len(s)):
            char = s[r_pointer]
            needDict[char] = 1 + needDict.get(char, 0)

            if char in haveDict and needDict[char] == haveDict[char]:
                have += 1

            while have == need:
                if r_pointer - l_pointer + 1 < ansLength:
                    ans, ansLength = [l_pointer, r_pointer], (r_pointer - l_pointer + 1)
                
                needDict[s[l_pointer]] -= 1
                if s[l_pointer] in haveDict and needDict[s[l_pointer]] < haveDict[s[l_pointer]]:
                    have -= 1
                l_pointer += 1
        
        l_pointer, r_pointer = ans
        return s[l_pointer:r_pointer + 1] if ansLength != float("infinity") else ""
