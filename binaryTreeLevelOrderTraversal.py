# 102. Binary Tree Level Order Traversal (BFS)

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
	res = []
	q = collections.deque()
	q.append(root)
	while q:
		qLen = len(q)
		level = []
		for i in range(qLen):
			node = q.popleft()
			if node:
				level.append(node.val)
				q.append(node.left)
				q.append(node.right)
		if level:
			res.append(level)
	return res