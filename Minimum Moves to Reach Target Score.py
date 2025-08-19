class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        # work backwards -> if target is even -> can remove a double, if it is odd then its best to decrement by 1 to get back to an even number. 
        # that should produce the min number of moves
        num = target
        rem_doubles = maxDoubles
        res = 0
        while num > 1:
            if num % 2 != 0:
                num -= 1
            elif num % 2 == 0 and rem_doubles:
                num //= 2
                rem_doubles -= 1
            else:
                res += num - 1
                break
            res += 1
        return res
                
