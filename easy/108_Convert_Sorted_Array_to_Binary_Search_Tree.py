# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def createTree(nums):
            node = None
            if len(nums) > 0:
                node = TreeNode(0)
                node.val = nums[len(nums) // 2]
                node.left = createTree(nums[:len(nums) // 2])
                node.right = createTree(nums[len(nums) // 2 + 1:])

            return node
        return createTree(nums)
