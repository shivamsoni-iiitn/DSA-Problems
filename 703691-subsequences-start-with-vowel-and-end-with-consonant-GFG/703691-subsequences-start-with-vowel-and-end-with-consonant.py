class Solution:
    def check(self, s):
        vowels='aeiou'
        if s[0] in vowels and s[-1] not in vowels:
            return True
        return False
        
    def helper(self, idx, s, curr, result):
        if idx>=len(s):
            x="".join(curr)
            if len(curr)!=0 and self.check("".join(curr)):
                result.append(x)
            return
        curr.append(s[idx])
        self.helper(idx+1, s, curr, result)
        curr.pop()
        self.helper(idx+1, s, curr, result)
    
    def findSubseq(self, s):
        # code here
        
        result=[]
        self.helper(0,s,[],result)
        return sorted(set(result))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna