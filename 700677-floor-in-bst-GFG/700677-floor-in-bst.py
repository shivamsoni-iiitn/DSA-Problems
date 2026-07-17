'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        #code here
        if root==None:
            return -1
        curr=-1
        while root!=None:
            if root.data==k:
                return root.data
            elif root.data<k:
                curr=root.data
                root=root.right
            else: 
                
                root=root.left
        return curr

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna