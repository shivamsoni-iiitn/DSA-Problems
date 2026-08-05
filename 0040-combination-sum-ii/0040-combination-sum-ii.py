class Solution:
    def helper(self, nums, target, idx,curr, result):
        if target==0:
            result.append(list(curr))
            return
        for i in range(idx,len(nums)):
            if i>idx and nums[i]==nums[i-1]:
                continue
            if nums[i]>target:
                break
            curr.append(nums[i])
            self.helper(nums, target-nums[i], i+1, curr, result)
            curr.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        self.helper(candidates, target, 0,[], result)
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna