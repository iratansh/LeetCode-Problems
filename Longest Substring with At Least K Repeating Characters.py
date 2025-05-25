class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        maxLen = 0 # store maxLen of substring

        for target_unique_chars in range(1, 27):  # number of unique characters
            window_count = defaultdict(int)
            l = r = 0
            unique = 0
            count_at_least_k = 0

            while r < len(s):
                # expand the window to the right
                window_count[s[r]] += 1
                if window_count[s[r]] == 1:
                    unique += 1 
                if window_count[s[r]] == k:
                    count_at_least_k += 1
                r += 1
                
                # shrink the window from the left if needed
                while unique > target_unique_chars:
                    if window_count[s[l]] == k:
                        count_at_least_k -= 1
                    window_count[s[l]] -= 1
                    if window_count[s[l]] == 0:
                        unique -= 1
                    l += 1
                
                # check validity and update maxLen
                if unique == count_at_least_k == target_unique_chars:
                    maxLen = max(maxLen, r - l)
        return maxLen
