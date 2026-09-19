class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(0, len(nums)):
            if (nums[i] == target):
                return i
            elif (nums[i] >= target):
                return i
            else:
                x = i + 1       
        return x           
                    
        