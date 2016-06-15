#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val == q.val:
            return ( self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) )
        
        return False


s = Solution()

leftTree = TreeNode(0)
leftTree.left = TreeNode(1)

rightTree= TreeNode(0)
rightTree.left = TreeNode(1)

print s.isSameTree(leftTree, rightTree) == True

rightTree.left = TreeNode(2)

print s.isSameTree(leftTree, rightTree) == False
