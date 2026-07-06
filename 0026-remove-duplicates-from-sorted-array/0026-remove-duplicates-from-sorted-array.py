class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        j=0
        for i in range(1,n):
            if nums[j]!=nums[i]:
                j+=1
                nums[j]=nums[i]
        return j+1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna