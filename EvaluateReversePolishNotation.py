class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for el in tokens:
                if el == '*':
                    stack.append(stack.pop() * stack.pop())
                elif el =='+':
                    stack.append(stack.pop() + stack.pop())
                elif el =='/':
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b / a))
                elif el == '-':
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                else:
                    stack.append(int(el))
        return stack[0] 
