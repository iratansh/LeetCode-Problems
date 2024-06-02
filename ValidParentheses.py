class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) % 2 == 0:
            for el in s:
                if el == "(" or el == "[" or el == "{":
                    stack.append(el)
                elif stack and el == ")" and stack[-1] == "(":
                    stack.pop()
                elif stack and el == "]" and stack[-1] == "[":
                    stack.pop()
                elif stack and el == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            return len(stack) == 0
        return False
