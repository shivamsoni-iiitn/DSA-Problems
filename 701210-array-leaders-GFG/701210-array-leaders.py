class Solution:
    def leaders(self, arr):
        # code here
        l=[]
        if not arr:
            return l
        n=len(arr)
        max_val=arr[n-1]
        l.append(max_val)
        for i in range(n-2,-1,-1):
            if(arr[i]>=max_val):
                l.append(arr[i])
                max_val=arr[i]
        l.reverse()
        return l

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna