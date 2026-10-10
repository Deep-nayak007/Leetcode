class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Create an empty dictionary to act as our tally sheet
        counts = {}
        
        # Step 1: Count how many times each number appears
        for i in nums:
            if i in counts:
                counts[i] += 1  # If we've seen it, add 1 to its tally
            else:
                counts[i] = 1   # If it's the first time, set tally to 1
                
        # Step 2: Look through our tally sheet to find the one with a count of 1
        for i in counts:
            if counts[i] == 1:
                return i