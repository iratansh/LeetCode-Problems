class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        count = 0
        l_g, l_s = 0, 0
        
        while l_g < len(g) and l_s < len(s):
            if s[l_s] >= g[l_g]:
                count += 1
                l_g += 1
            l_s += 1
        
        return count
