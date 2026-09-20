class Solution:
    def reverseDegree(self, s: str) -> int:
        val=0
        for i in range(len(s)):
            val+=(i+1)*(26-(ord(s[i])-ord('a')))
        return val

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna