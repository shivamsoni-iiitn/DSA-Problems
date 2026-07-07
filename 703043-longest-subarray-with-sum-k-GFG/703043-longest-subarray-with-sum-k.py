class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        mpp : dict[int,int]={}
        n=len(arr)
        maxi=0
        sume=0
        for i in range(n):
            sume+=arr[i]
            if sume==k:
                maxi=max(maxi,i+1)
            rem=sume-k
            if rem in mpp:
                maxi=max(maxi, i-mpp[rem])
            if sume not in mpp:
                mpp[sume]=i
        return maxi

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna