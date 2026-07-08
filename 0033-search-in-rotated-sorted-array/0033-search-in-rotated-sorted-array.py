class Solution(object):
    def apply(self, l,r,nums, target):
        while(l<=r):
            mid=l+(r-l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]< target:
                l=mid+1
            else:
                r=mid-1
        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r=0, len(nums)-1
        
        while(l<=r):
            mid=l+(r-l)//2
            if nums[l]<=nums[mid]:
                if target>=nums[l] and nums[mid]>=target:
                    return self.apply(l, mid,nums, target)
                    
                l=mid+1
            else:
                if nums[mid]<=target<=nums[r]:
                    return self.apply(mid, r, nums, target)
                    
                r=mid-1
        
        return -1



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna