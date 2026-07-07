class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mpp={}
        n=len(nums)
        for i in range(n):
            rem=target-nums[i]
            if rem in mpp:
                return [mpp[rem],i]
            else:
                mpp[nums[i]]=i
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna