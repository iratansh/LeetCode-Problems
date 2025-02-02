class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":  
            return 0  
        
        table = [0] * (len(s) + 1)
        table[0] = 1  
        table[1] = 1 
        
        for i in range(2, len(s) + 1):  
            if s[i - 1] != "0":  
                table[i] += table[i - 1]  
            two_digit = int(s[i - 2:i])  # Check the last two characters
            if 10 <= two_digit <= 26:
                table[i] += table[i - 2]  # Two-digit decoding
        return table[-1]
