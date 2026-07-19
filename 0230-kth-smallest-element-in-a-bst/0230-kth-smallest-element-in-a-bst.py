# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            self.k-=1
            if self.k==0:
                self.res=root.val
                return self.res
            self.inorder(root.right)


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res=None
        self.k=k
        self.inorder(root)
        return self.res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna