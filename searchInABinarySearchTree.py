# 700. Search in a Binary Search Tree

# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    def dfs(node):
        if not node:
            return
        if node.val == val:
            return node
        if node.val < val:
            return dfs(node.right)
        else:
            return dfs(node.left)
        
    return dfs(root)