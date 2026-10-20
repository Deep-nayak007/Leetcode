class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = sorted(nums)
        m = []
        for i in range(len(nums)):
            if (target == x[i]):
                m.append(i)

        return m       

        