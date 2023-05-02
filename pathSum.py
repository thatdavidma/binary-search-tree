# 112. Path Sum

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

    if not root: return False

    def dfs(node, sum):
        if not node and sum != targetSum: return False
        if sum == targetSum: return True
        else:
            return dfs(node.left, sum + node.val) or dfs(node.right, sum + node.val)
    
    return dfs(root, 0)