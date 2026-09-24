class Solution:
    def summation(self, num):
        summ=0
        num=abs(num)
        while(num!=0):
            summ+=num%10
            num=num//10
        return summ

    def smallestIndex(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            if self.summation(nums[i])==i:
                return i
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna