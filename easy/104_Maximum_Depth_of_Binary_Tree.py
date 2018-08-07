# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def height(t, sum):
            if t:
                return max(height(t.left, sum + 1), height(t.right, sum + 1))
            return sum
        return height(root, 0)
