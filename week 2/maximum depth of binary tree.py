# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #dfs

        def helper(node):
            #base case
            if not node:
                return 0
            

            depth = max(helper(node.left), helper(node.right))
            return depth + 1
        return helper(root)        
