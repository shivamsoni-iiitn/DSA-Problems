class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        maxi=0
        l,r=0,0
        mpp=defaultdict(int)
        while r<n:
            mpp[fruits[r]]+=1
            if len(mpp)>2:
                mpp[fruits[l]]-=1
                if mpp[fruits[l]]==0:
                    del mpp[fruits[l]]
                l+=1
            maxi=max(maxi, r-l+1)
            r+=1
        return maxi

        # for i in range(n):
        #     s=set()
        #     for j in range(i,n):
        #         if len(s)>2:
        #             break
        #         s.add(fruits[j])
        #         maxi=max(maxi, j-i+1)
        # return maxi


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna