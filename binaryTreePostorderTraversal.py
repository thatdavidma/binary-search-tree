# 145. Binary Tree Postorder Traversal

# Given the root of a binary tree, return the postorder traversal of its nodes' values.

def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
	stack = [root]
	visit = [False]
	res = []
	
	while stack:
		cur, v = stack.pop(), visit.pop()
		if cur:
			if v:
				res.append(cur.val)
			else:
				stack.append(cur)
				visited.append(True)
				stack.append(cur.right)
				visit.append(False)
				stack.append(cur.left)
				visit.append(False)
	
	return res