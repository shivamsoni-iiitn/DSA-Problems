class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        n=len(s)
        for i in s:
            if i in "({[":
                st.append(i)
            else:
                if not st:
                    return False
                top=st.pop()

                if (i==')' and top=='(') or (i=='}' and top=='{') or (i==']' and top=='['):
                    continue
                else:
                    return False
        return len(st)==0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna