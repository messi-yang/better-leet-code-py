# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
        	return 0
        dL = self.maxDepth(root.left)+1
        dR = self.maxDepth(root.right)+1

        return dL if dL>=dR  else dR

#Test cases

#create on node and reserve it's parent node as nodeParent
node = TreeNode(1)
nodeParent = node

node.left = TreeNode(2)
node.right = TreeNode(3)
node = node.left
node.left = TreeNode(4)

solution = Solution()
print solution.maxDepth(nodeParent) == 3

node = node.left
node.left = TreeNode(5)

print solution.maxDepth(nodeParent) == 4

node = node.left
node.left = TreeNode(6)

print solution.maxDepth(nodeParent) == 5
