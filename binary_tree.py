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
    def levelorderTravel(self,root):
        #层序遍历，循环，广度优先搜索
        if not root:
            return []
        ret = []
        level = [root]
        while level:
            current = []
            next_level = []
            for l in level:
                current.append(l.val)
                if l.left:
                    next_level.append(l.left)
                if l.right:
                    next_level.append(l.right)
            ret.append(current)
            level = next_level
        return ret