class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0 
        nums.sort()
        longest = 1
        count = 1
        x = nums[0]
        for i in range(1, len(nums)):
            y = x + 1

            if(nums[i] == y):
                count += 1
                x = y
            elif(nums[i] == x):
                continue
            else:
                x = nums[i]
                count = 1
            longest = max(longest, count)
        return longest                       
        