from collections import deque
from typing import List, Optional
from dataStructures.BinaryTree import TreeNode

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res, q = [], deque([root])

        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i == size - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res