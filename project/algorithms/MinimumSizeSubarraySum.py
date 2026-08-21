from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min = float("inf")
        left = 0
        sum = 0

        for right in range(len(nums)):
            sum += nums[right]

            while sum >= target:
                if right - left + 1 < min:
                    min = right - left + 1
                sum -= nums[left]
                left += 1
        
        return min if min != float("inf") else 0