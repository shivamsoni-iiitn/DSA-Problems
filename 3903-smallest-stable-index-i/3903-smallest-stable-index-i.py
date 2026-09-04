class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        arr=[-1]*n
        mini=nums[n-1]
        for i in range(n-1,-1,-1):
            arr[i]=min(nums[i],mini)
            mini=arr[i]
        maxi=nums[0]
        for i in range(n):
            maxi=max(maxi, nums[i])
            val=maxi-arr[i]
            if val<=k:
                return i
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna