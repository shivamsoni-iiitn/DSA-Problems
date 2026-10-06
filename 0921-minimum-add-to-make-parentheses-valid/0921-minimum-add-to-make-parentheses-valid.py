class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[]
        closed=0
        for i in range(len(s)):
            if s[i]=='(':
                st.append('(')
            elif s[i]==')':
                if st and st[-1]=='(':
                    st.pop()
                elif not st:
                    closed+=1
        
        
        return len(st)+closed
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna