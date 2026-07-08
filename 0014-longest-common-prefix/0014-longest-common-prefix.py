class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first=strs[0]
        last=strs[len(strs)-1]
        upto=min(len(first), len(last))
        res=""
        for i in range(upto):
            if first[i]!=last[i]:
                break
            else:
                res+=first[i]
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna