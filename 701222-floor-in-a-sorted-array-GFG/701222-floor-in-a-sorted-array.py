class Solution:
    def findFloor(self, arr, x):
        # code here
        l,r= 0, len(arr)-1
        while l<=r:
            mid=l+(r-l)//2
            if arr[mid]>x:
                r=mid-1
            else:
                l=mid+1
        return r

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna