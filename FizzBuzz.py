class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        
        for i in range(1, n + 1):
            fizz = ""

            if i % 3 == 0:
                fizz += "Fizz"
            
            if i % 5 == 0:
                fizz += "Buzz"
            
            if len(fizz) == 0:
                fizz = str(i)
            
            arr.append(fizz)
        
        return arr
