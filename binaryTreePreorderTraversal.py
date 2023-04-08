# Binary Search Tree

# 144. Binary Tree Preorder Traversal

# Given the root of a binary tree, return the preorder traversal of its nodes' values.

def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    head = root
    stack = []
    res = []

    # Preorder Traversal means root --> left --> right
    # We append the right side to the stack in order to pop it off later
    while head or stack:
        if head:
            res.append(head.val)
            if head.right:
                stack.append(head.right)
            head = head.left
        else:
            head = stack.pop()

    return res