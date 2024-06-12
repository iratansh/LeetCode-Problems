class Solution:
    def isHappy(self, n: int) -> bool:
        num = 0
        num_dict = {}
        s_n = str(n)
        while True:
            for el in str(s_n):
                num += int(el) ** 2
            if num == 1:
                return True
            if num in num_dict:
                return False
            num_dict[num] = 0
            s_n = num
            num = 0
