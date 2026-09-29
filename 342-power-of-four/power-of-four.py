class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if (n == 0):
            return False
        if (n == -1):
            return False
        if (n == 1):
            return True    
        for i in range(1, n):
            if (4**i == n):
                return True 
            if (4**i > n):
                return False    
        return False                     
        
        