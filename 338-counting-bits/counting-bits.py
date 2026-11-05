class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(0, n+1):
            num = i
            count = 0
            while(num>0):
                num = num & (num - 1)
                count = count + 1
            ans.append(count)
        return ans        
        