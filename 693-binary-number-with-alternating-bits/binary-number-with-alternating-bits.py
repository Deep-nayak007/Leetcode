class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ans = bin(n)[2:]
        for i in range(len(ans) - 1):
            if (ans[i] == ans[i+1]):
                return False
        return True        

        