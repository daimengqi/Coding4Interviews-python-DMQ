class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 返回构造的TreeNode根节点
def reConstructBinaryTree(pre, tin):
    # write code here
    if not pre:
        return None
    root_val = pre[0]
    root = TreeNode(root_val)
    for i in range(len(tin)):
        if tin[i] == root_val:
            break
    root.left = reConstructBinaryTree(pre[1:1+i], tin[:i])
    root.right = reConstructBinaryTree(pre[1+i:], tin[i+1:])
    
    return root

def preorder(root):
    if root:
        preorder(root.left)
        print(root.val)
        preorder(root.right)
preorder(reConstructBinaryTree([1,2,3,4,5,6,7],[3,2,4,1,6,5,7]))

# 解法二
def reConstructBinaryTree(self, pre, tin):
	# write code here
	if not pre or not tin:
		return None 
	# 树用递归实现
	# 先序遍历序列第一个是根节点，中序遍历序列中，根节点前面的是根节点的左子树，后面的是其右子树
	root = TreeNode(pre.pop(0))
	index = tin.index(root.val)
	root.left = self.reConstructBinaryTree(pre, tin[0:index])
	root.right = self.reConstructBinaryTree(pre, tin[index+1:])
	return root