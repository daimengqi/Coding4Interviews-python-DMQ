class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isEqual(p1, p2):
    if not p1 and not p2:
        return True
    elif p1 and p2 and p1.val == p2.val:
        return True
    else:
        return False

class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot: return True
        queue = [pRoot]
        while queue:
            n = len(queue)
            if queue[0] != pRoot and n % 2 != 0: 
                return False
            for i in range(n//2):
                if not isEqual(queue[i], queue[-1-i]):
                    return False
            for _ in range(n):
                node = queue.pop(0)
                if not node: continue
                queue.append(node.left)
                queue.append(node.right)
        return True

# 解法二
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        # 根节点及其左右子树，左子树的右子树与右子树的左子树相同且左子树的左子树与右子树的右子树相同即对称，采用递归
        return self.isSame(pRoot, pRoot)
    def isSame(self, root1, root2):
        if (not root1) and (not root2):
            return True
        if (not root1) or (not root2):
            return False
        if root1.val != root2.val:
            return False
        return self.isSame(root1.left, root2.right) and self.isSame(root1.right, root2.left)
          
          
        