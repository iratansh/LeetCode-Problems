class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l_pointer = 0
        ans = 0
        
        for r_pointer in range(len(s)):
            while s[r_pointer] in chars:
                chars.remove(s[l_pointer])
                l_pointer += 1
            chars.add(s[r_pointer])
            ans = max(ans, r_pointer - l_pointer + 1)
        return ans
