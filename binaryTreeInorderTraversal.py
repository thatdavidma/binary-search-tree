# 94. Binary Tree Inorder Traversal

# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# # Inorder means: Left subtree --> Root --> Right subtree

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []

    def inorder(root):
        if not root:
            return
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)

    inorder(root)
    return res