class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        a=-1
        count=0
        for i in range(n):
            if nums[i]!=0:
                a+=1
                nums[a]=nums[i]
                
            else:
                count+=1
        
        for i in range(a+1,n):
            nums[i]=0
        return nums

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna