class Solution:
    def helper(self, nums, idx, curr, result):
        result.append(list(curr))
        
        for i in range(idx,len(nums)):
            if i>idx and nums[i]==nums[i-1]:
                continue
            curr.append(nums[i])
            self.helper(nums, i+1, curr,result)
            curr.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        self.helper(nums, 0,[],result)
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna