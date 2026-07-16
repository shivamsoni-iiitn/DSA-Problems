'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def topView(self, root):
        # code here
        ans=[]
        if root==None:
            return ans
        q=deque()
        mpp={}
        q.append((root,0))
        while q:
            node,hd=q.popleft()
            if hd not in mpp:
                mpp[hd]=node.data
            if node.left:
                q.append((node.left, hd-1))
            if node.right:
                q.append((node.right, hd+1))
            
        for it in sorted(mpp.keys()):
            ans.append(mpp[it])
        return ans
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna