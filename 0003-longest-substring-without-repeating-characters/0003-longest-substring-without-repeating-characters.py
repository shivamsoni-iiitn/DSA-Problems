class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi=0
        l,r=0,0
        n=len(s)
        hash=[-1]*256
        while r<n:
            if hash[ord(s[r])]!=-1:
                l=max(hash[ord(s[r])]+1,l)
            hash[ord(s[r])] = r
            maxi=max(maxi, r-l+1)
            r+=1
        return maxi


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna