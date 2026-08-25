from typing import List

class Solution(object):
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        
        for i, num in enumerate(nums):
            if seen.get(num) != None and i - seen[num] <= k:
                return True
            seen[num] = i
        return False

    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
        
        seen = {}
        for i, x in enumerate(nums): 
            n = x // (valueDiff+1)
            if n in seen and i - seen[n][0] <= indexDiff:
                return True 
            if n-1 in seen and i - seen[n-1][0] <= indexDiff and abs(x - seen[n-1][1]) <= valueDiff:
                return True 
            if n+1 in seen and i - seen[n+1][0] <= indexDiff and abs(x - seen[n+1][1]) <= valueDiff:
                return True 
            seen[n] = (i, x) 
        return False 