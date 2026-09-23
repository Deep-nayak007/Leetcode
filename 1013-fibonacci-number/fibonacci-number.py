class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        x = 0
        y = 1
        output = x + y
        for i in range(2, n+1):
            z = x + y
            output = output + z

            x = y
            y = z
            
        return y   


        