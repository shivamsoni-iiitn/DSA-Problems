class Solution:
    def f(self, nums,k):
        n=len(nums)
        l,r=0,0
        sum,count=0,0
        if k<0:
            return 0
        while r<n:
            if nums[r]%2!=0:
                sum+=1
            else:
                sum+=0
            while sum>k:
                if nums[l]%2!=0:
                    sum-=1
                else:
                    sum-=0
                l+=1
            count+=r-l+1
            r+=1
        return count

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.f(nums,k)-self.f(nums,k-1)

        # for i in range(n):
        #     odd=0
        #     for j in range(i,n):
        #         if nums[j]%2!=0:
        #             odd+=1
        #         if odd>k:
        #             break
        #         if odd==k:
        #             count+=1
                
        # return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna