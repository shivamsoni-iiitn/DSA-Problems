class Solution:
    def findKRotation(self, arr):
        # code here
        l,r=0, len(arr)-1
        while(l<r):
            mid=l+(r-l)//2
            if(arr[mid]>arr[r]):
                l=mid+1
            else:
                r=mid
        return l

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna