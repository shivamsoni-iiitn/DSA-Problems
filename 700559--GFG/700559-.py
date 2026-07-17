'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def findMin(self,root):
        #code here
        # mini=float('inf')
        if root==None:
            return float('inf')
        return min(root.data, self.findMin(root.left),self.findMin(root.right))
        
    def findMax(self,root):
        #code here
        # maxi=float('-inf')
        if root==None:
            return float('-inf')
        return max(root.data, self.findMax(root.left),self.findMax(root.right))
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna