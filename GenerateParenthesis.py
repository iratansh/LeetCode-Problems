class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []

        def backtrack(nOpened, nClosed):
            if nOpened == nClosed == n:
                ans.append("".join(stack))
                return 
             
            if nOpened < n:
                stack.append('(')
                backtrack(nOpened + 1, nClosed)
                stack.pop()
            
            if nClosed < nOpened:
                stack.append(')')
                backtrack(nOpened, nClosed + 1)
                stack.pop()

        backtrack(0, 0)
        return ans
