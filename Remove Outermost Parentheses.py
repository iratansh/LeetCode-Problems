class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # as depth increases that means you become more nested inside the parentheses
        # only append the parentheses that are not outermost 
        res = []
        depth = 0
        for char in s:
            if char == '(': # if its an opening bracket increase depth 
                if depth > 0:
                    res.append(char)
                depth += 1
            else: # if its a closing bracket decrease depth
                depth -= 1
                if depth > 0:
                    res.append(char)
        return "".join(res)
