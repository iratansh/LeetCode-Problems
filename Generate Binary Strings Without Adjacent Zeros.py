class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1"]

        combs = []
        def backtrack(curr):
            if len(curr) == n:
                combs.append(curr)
                return

            backtrack(curr + "1")

            # Add '0' only if previous char wasn't '0'
            if not curr or curr[-1] != "0":
                backtrack(curr + "0")
        
        backtrack("")
        return combs

