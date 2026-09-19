from dataStructures.BinaryTree import TreeNode

class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        self.count = k

        def inorder(node):
            if node == None:
                return None

            val = inorder(node.left)
            if val != None:
                return val

            if self.count-1 > 0:
                self.count-=1
            else:
                return node.val

            return inorder(node.right)

        return inorder(root)