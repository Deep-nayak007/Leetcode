class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = sorted(nums)
        if x[0] != 0:
            return 0
        for i in range(len(x) - 1):
            if x[i] + 1 != x[i + 1]:
                return x[i] + 1
        return len(x)              