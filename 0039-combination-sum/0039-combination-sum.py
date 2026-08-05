class Solution:
    def helper(self, nums, target, idx, curr, result):
        if idx>=len(nums):
            if target==0:
                result.append(list(curr))
            return
        if nums[idx]<=target:
            curr.append(nums[idx])
            self.helper(nums, target-nums[idx],idx, curr, result)
            curr.pop()
        self.helper(nums, target,idx+1, curr, result)
        

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        self.helper(candidates, target, 0, [], result)
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna