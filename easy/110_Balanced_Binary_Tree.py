# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def caculHeight(node):
            if node is None:
                return 0
            return max(caculHeight(node.left), caculHeight(node.right)) + 1

        def judge(node):
            if node is None:
                return True
            if abs(caculHeight(node.left) - caculHeight(node.right)) > 1:
                return False
            else:
                return judge(node.left) and judge(node.right)
        return judge(root)
