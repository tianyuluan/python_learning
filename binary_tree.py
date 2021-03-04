class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self,root):
        #前序遍历,递归
        def preorder(root):
            if not root:return []
            result.append(root.val)
            preorder(root.left)
            preorder(root.right)
        result = []
        preorder(root)
        return result
    def middleorderTraveral(self,root):
        #中序遍历，递归
        def preorder(root):
            if not root:return []
            preorder(root.left)
            result.append(root.val)
            preorder(root.right)
        result = []
        preorder(root)
        return result
    def postorderTraveral(self,root):
        #后序遍历，递归
        def preorder(root):
            if not root:return []
            preorder(root.left)
            preorder(root.right)
            result.append(root.val)
        result = []
        return result