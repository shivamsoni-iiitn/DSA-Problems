class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        maxidx=0
        for i in range(n):
            if i>maxidx:
                return False
            maxidx=max(maxidx, i+nums[i])
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna