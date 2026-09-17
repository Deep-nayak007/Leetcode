class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        if (len(nums) < 2):
            return 0
        output = 0    
         
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                num1 = nums[i]
                num2 = nums[j]
                correct = (num1 * num2) // (math.gcd(num1, num2) ** 2)
                output = max(output, correct)
        return output 
