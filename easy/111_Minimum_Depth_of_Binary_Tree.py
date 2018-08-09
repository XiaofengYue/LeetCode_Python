# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from queue import Queue


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = Queue()
        q.put(root)
        height = 0
        while not q.empty():
            nowSize = q.qsize()
            height += 1
            for _ in range(nowSize):
                x = q.get()
                if x.left:
                    q.put(x.left)
                if x.right:
                    q.put(x.right)
                if not x.left and not x.right:
                    return height
