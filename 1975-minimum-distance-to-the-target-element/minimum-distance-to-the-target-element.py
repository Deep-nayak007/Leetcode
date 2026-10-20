class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        m = []
        for i in range(len(nums)):
            if(target == nums[i]):
                m.append(abs(i - start))
        return min(m)

        