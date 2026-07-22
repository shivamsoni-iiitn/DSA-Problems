class Solution:
    def nge(self, nums):
        n=len(nums)
        st=[]
        mpp=defaultdict(int)
        for i in range(n-1,-1,-1):
            while (st and st[-1]<=nums[i]):
                st.pop()
            
            if not st:
                mpp[nums[i]]=-1
                
            else:
                mpp[nums[i]]=st[-1]
            st.append(nums[i])
        return mpp

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mpp=self.nge(nums2)
        arr=[-1]*len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in mpp:
                arr[i]=mpp[nums1[i]]
        return arr

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna