class Solution:
    def f(self,nums,goal):
        count=0
        n=len(nums)
        l,r=0,0
        sum=0
        if goal<0:
            return 0
        while(r<n):
            sum+=nums[r]
            while sum>goal:
                sum-=nums[l]
                l+=1
            count=count+(r-l+1)
            r+=1
        return count


    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.f(nums,goal)-self.f(nums,goal-1)

        # for i in range(n):
        #     sum=0
        #     for j in range(i,n):
        #         sum+=nums[j]
        #         if sum==goal:
        #             count+=1
        # return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna