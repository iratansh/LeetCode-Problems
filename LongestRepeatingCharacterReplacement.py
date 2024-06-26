class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l_pointer = 0
        count = {}
        ans = 0

        for r_pointer in range(len(s)):
            count[s[r_pointer]] = 1 + count.get(s[r_pointer], 0)
            if (r_pointer - l_pointer + 1) - max(count.values()) > k:
                count[s[l_pointer]] -= 1
                l_pointer += 1
            ans = max(ans, r_pointer - l_pointer + 1)
        return ans
