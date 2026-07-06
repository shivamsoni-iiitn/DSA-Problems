class Solution:
    def getSecondLargest(self, arr):
        # code here
        maxi=float('-inf')
        smax=float('-inf')
        n=len(arr)
        if n<2:
            return -1
        for i in range(n):
            if(arr[i]>maxi):
                smax=maxi
                maxi=arr[i]
                
            elif(arr[i]>smax and maxi!=arr[i]):
                smax=arr[i]
        if smax==float('-inf'):
            return -1
        return smax

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna