class Solution:
    def climbStairs(self, n: int) -> int:
        prev2,prev=1,1
        for i in range(2,n+1):
            curr=prev2+prev
            prev2=prev
            prev=curr
        return prev

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna