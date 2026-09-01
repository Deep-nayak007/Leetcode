class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pos = len(digits) - 1
        while (pos) >= 0:
            if digits[pos] < 9:      
                digits[pos] = digits[pos] + 1
                return digits
            else:
                digits[pos] = 0
                pos = pos - 1
        return [1] + digits            


        