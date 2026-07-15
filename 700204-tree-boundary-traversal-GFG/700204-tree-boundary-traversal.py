'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def isLeaf(self, root):
        return not root.left and not root.right
    
    def addLeft(self, root,res):
        curr=root.left
        
        while(curr):
            if not self.isLeaf(curr):   
                res.append(curr.data)
            if curr.left:
                curr=curr.left
            else:
                curr=curr.right
    
    def addRight(self,root,res):
        temp=[]
        curr=root.right
        while(curr):
            if not self.isLeaf(curr):
                temp.append(curr.data)
            if curr.right:
                curr=curr.right
            else:
                curr=curr.left
        for i in range(len(temp)-1,-1,-1):
            res.append(temp[i])
        
    def addLeaf(self,root,res):
        curr=root
        if self.isLeaf(curr):
            res.append(curr.data)
        if curr.left:
            self.addLeaf(curr.left, res)
        if curr.right:
            self.addLeaf(curr.right,res)
        
        
    def boundaryTraversal(self, root):
        # code here
        res=[]
        if not root:
            return []
        if not self.isLeaf(root):
            res.append(root.data)
        
        self.addLeft(root, res)
        self.addLeaf(root, res)
        self.addRight(root,res)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna