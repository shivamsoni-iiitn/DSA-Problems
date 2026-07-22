class Solution:
    def nge(self, nums):
        st=[]
        n=len(nums)
        arr=[0]*n
        for i in range(2*n-1,-1,-1):
            while st and st[-1]<=nums[i%n]:
                st.pop()
            if not st:
                arr[i%n]=-1
            else:
                arr[i%n]=st[-1]
            st.append(nums[i%n])
        return arr
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        return self.nge(nums)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna