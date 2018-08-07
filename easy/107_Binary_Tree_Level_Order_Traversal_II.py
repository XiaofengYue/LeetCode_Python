# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        list_l = []

        def traveral(p, depth):
            if p:
                if depth >= len(list_l):
                    list_l.append([])
                if p.left:
                    traveral(p.left, depth + 1)
                if p.right:
                    traveral(p.right, depth + 1)
                list_l[depth].append(p.val)
        traveral(root, 0)
        return list_l[::-1]
