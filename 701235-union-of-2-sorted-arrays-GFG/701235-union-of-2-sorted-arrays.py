class Solution:
    def findUnion(self, a, b):
        # code here 
        n=len(a)
        m=len(b)
        freq={}
        for i in range(n):
            freq[a[i]]=freq.get(a[i],0)+1
        for i in range(m):
            freq[b[i]]=freq.get(b[i],0)+1
            
        unioun=sorted(freq.keys())
        return unioun

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna