class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr=[]
        n=len(nums)
        mini=nums[0]
        maxi=nums[1]
        for i in range(0,n-1):
            while(mini+1!=nums[i+1]):
                arr.append(mini+1)
                x=mini+1
                mini=x
            mini=nums[i+1]
        return arr

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna