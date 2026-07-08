class Solution:
    def upperBound(self, arr, target):
        # code here
        l,r=0, len(arr)-1
        while l<=r:
            mid=l-(l-r)//2
            if arr[mid]<=target:
                l=mid+1
    
            else:
                r=mid-1
        
        return l

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna