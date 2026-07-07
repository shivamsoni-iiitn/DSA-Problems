class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        el=-1
        count=0
        n=len(nums)
        for i in range(n):
            if count==0:
                el=nums[i]
                count=1
            elif nums[i]==el:
                count+=1
            else:
                count-=1
        
        c1=0
        for num in nums:
            if el==num:
                c1+=1
        
        if c1>n//2:
            return el



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna