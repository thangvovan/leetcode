from typing import Optional
from dataStructures.BinaryTree import TreeNode


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1

        height = 0
        node = root
        while node.left != None:
            node = node.left
            height+=1

        def count(root, left, right, h):
            if root.left == None and root.right == None:
                return 2
            elif root.left == None or root.right == None:
                return 1

            if left == 0:
                node = root
                while node.left != None:
                    node = node.left
                    left+=1
            if right == 0:
                node = root
                while node.right != None:
                    node = node.right
                    right+=1

            if left == right:
                if left != h:
                    return (2**(left+1))
                return 0
            else:
                c = count(root.left, left-1, 0, h-1)
                if c == 0:
                    return count(root.right, 0, right-1, h-1)
                else:
                    return c + 2**right

        return (2**(height+1)-1) - count(root, height, 0, height)