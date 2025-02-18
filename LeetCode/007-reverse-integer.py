class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg=1
        if(x<0):
            x = x*-1
            neg=-1
        q = x/10
        r = x%10
        exp = 0
        y=0
        while q is not 0:
            
            y = y*(10**exp)+r
            r = q%10
            q = q/10
            exp = 1
            
        y = (y*(10**exp)+r) * neg
        if y<-2**31 or y >2**31-1:
            return 0

        return y