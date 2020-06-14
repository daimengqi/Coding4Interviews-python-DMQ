# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.pre = None
        
    def Convert(self, root):
        # write code here
        if not root: return None
        self.helper(root)
        while root.left:
            root = root.left
        return root

    def helper(self, cur):
        if not cur: return None
        self.helper(cur.left)
        cur.left = self.pre
        if self.pre:
            self.pre.right = cur
        self.pre = cur
        self.helper(cur.right)

# �ⷨ��
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # �½����� �洢���ڵ㣬Ҳ�Ǵ洢˫������
    def __init__(self):
        self.arr = []
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        # ������������������������ڵ�˳��洢
        self.midTraversal(pRootOfTree)
        # ˫��������ָ������Ԫ�ظ�����һ
        for i, v in enumerate(self.arr[: -1]):
            # ˫�������ڵ���Һ���Ҳ��������ָ�����һ���ڵ�
            v.right = self.arr[i+1]
            # ˫�������ڵ������Ҳ����������һ���ڵ�
            self.arr[i+1].left = v
        # ����洢˳�����ڵ㣬ͬʱҲ��˫������֪�����ĸ��ڵ㣬���������ı�ͷ��Ҳ���ܻ������˫������
        return self.arr[0]
    # ��������洢���Ľڵ�
    def midTraversal(self,root):
        if not root:
            return None
        self.midTraversal(root.left)
        self.arr.append(root)
        self.midTraversal(root.right)
        
