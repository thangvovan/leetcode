from typing import List, Optional
from dataStructures.BinaryTree import TreeNode

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[-1] 

    def rob2(self, nums: List[int]) -> int:
        def dynamic(nums):
            prev_rob = max_rob = 0

            for cur_val in nums:
                temp = max(max_rob, prev_rob + cur_val)
                prev_rob = max_rob
                max_rob = temp
            
            return max_rob
        
        return max(dynamic(nums[:-1]), dynamic(nums[1:]), nums[0])

    def rob3(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)

            rob_node = node.val + left_skip + right_skip
            skip_node = max(left_skip, left_rob) + max(right_skip, right_rob)

            return rob_node, skip_node
        
        rob_root, skip_root = dfs(root)

        return max(rob_root, skip_root)