# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root):
        if root==None:
            return 0
        left=max(0,self.check(root.left))
        right=max(0,self.check(root.right))
        self.maxi=max(root.val+left+right, self.maxi)
        return root.val+max(left,right)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi=float('-inf')
        self.check(root)
        return self.maxi

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna