class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = 0
        for i in digits:
            n  = n * 10 + i
        m = n + 1
        back_to_digits = [int(char) for char in str(m)]
        return(back_to_digits)






        