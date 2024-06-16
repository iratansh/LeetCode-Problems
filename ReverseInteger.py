class Solution:
    def reverse(self, x: int) -> int:
        stack = []
        if x < 0:
            temp = -1
            x = x * -1
            for el in str(x):
                stack.append(el)
            if temp * int(''.join(stack[::-1])) > 2 ** 31 - 1 or temp * int(''.join(stack[::-1])) < -2 ** 31:
                return 0
            return temp * int(''.join(stack[::-1]))
            

        else:
            for el in str(x):
                stack.append(el)
            if int(''.join(stack[::-1])) > 2 ** 31 - 1 or int(''.join(stack[::-1])) < -2 ** 31:
                return 0
            return int(''.join(stack[::-1]))
        
