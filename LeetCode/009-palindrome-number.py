class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        y = x
        r = 0
        while y > 0:
            r = r * 10 + y % 10
            y //= 10
        return x == r