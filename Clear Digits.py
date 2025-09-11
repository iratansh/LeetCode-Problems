class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        char_list = list(s)

        for i, el in enumerate(char_list):
            if el.isalpha():
                stack.append(el)
            if stack and el.isdigit():
                stack.pop()
        return "".join(stack)
