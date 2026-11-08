class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = []
        count = 1
        y = 0
        x = sorted(nums)
        for i in range(len(x)-1):
            if(x[i] == x[i+1]):
                count = count + 1
            else:
                counts.append([count, x[i]])
                count = 1
        counts.append([count, x[-1]])
        counts.sort(reverse = True)
        output = []
        for i in range(k):
            output.append(counts[i][1])
        return output    

        