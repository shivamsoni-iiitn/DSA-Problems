class Solution:
    def minCost(self, height: list[int]) -> int:
        # code here
        n=len(height)
        prev2=0
        if n<=1:
            return prev2
        
        prev=prev2+abs(height[0]-height[1])
        for i in range(2, n):
            one=prev+abs(height[i]-height[i-1])
            two=prev2+abs(height[i]-height[i-2])
            curr=min(one, two)
            prev2=prev
            prev=curr
        return prev

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna