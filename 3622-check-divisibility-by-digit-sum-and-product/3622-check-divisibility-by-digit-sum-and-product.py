class Solution(object):
    def digit_sum(self,n):
        s=0
        p=1
        while(n!=0):
            rem=n%10
            n=n/10
            s+=rem
            p*=rem
        return [s,p]
            
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x,y=self.digit_sum(n)
        if n%(x+y)==0:
            return True
        return False
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna