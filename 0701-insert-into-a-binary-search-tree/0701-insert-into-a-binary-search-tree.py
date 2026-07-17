# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
            return TreeNode(val)
        parent1=root
        parent=parent1
        while root!=None:
            parent=root
            if root.val>val:
                root=root.left
            elif root.val<val:
                root=root.right

        if parent.val>val:
            parent.left=TreeNode(val)
        else:
            parent.right=TreeNode(val)
        return parent1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna