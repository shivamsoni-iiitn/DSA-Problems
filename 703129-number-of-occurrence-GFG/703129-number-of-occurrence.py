class Solution:
    def floor(self, nums, target):
        l,r=0, len(nums)-1
        ans=-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                ans=mid
                r=mid-1

            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return ans


    def ceil(self, nums, target):
        l,r=0, len(nums)-1
        ans=-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                ans=mid
                l=mid+1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return ans
        
    def countFreq(self, arr, target):
        # code here
        x=self.floor(arr, target)
        y=self.ceil(arr, target)
        if x==y==-1:
            return 0
        return y-x+1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna