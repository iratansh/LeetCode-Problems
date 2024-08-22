class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combs = []
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        if digits == "":
            return []

        def backtrack(i, curr):
            if len(curr) == len(digits):
                combs.append(curr)
                return
            
            for el in keyboard[digits[i]]:
                backtrack(i + 1, curr + el)
        
        backtrack(0, "")
        return combs
