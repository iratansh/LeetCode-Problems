class Solution:
    def partitionString(self, s: str) -> int:
        res = 0  
        seen = set()

        for char in s:
            if char in seen:
                res += 1  
                seen.clear()  # Reset seen for the new partition

            seen.add(char)  # Add current character to the set

        return res + 1 
