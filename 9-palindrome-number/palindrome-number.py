class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
            
        original = x
        reversed_num = 0

        while x > 0:
            y = x % 10
            reversed_num = (reversed_num * 10) + y
            x = x // 10

        return original == reversed_num



        