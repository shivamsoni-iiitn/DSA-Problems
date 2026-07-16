"""
Definition of Node
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""
from collections import deque
class Solution:
    def inserting(self,root, small, nums):
        if root==None:
            return
        small.append(root.data)
        if root.left==None and root.right==None:
            nums.append(small.copy())
        else:
            self.inserting(root.left,small,nums)
            self.inserting(root.right,small,nums)
        small.pop()
    def paths(self, root):
        # code here
        small=[]
        nums=[]
        self.inserting(root,small,nums)
        return nums
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna