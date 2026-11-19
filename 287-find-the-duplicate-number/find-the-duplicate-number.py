class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = sorted(nums)
        for i in range(len(x) -1):
            if(x[i] == x[i+1]):
                return x[i]
        return 0           

        
        