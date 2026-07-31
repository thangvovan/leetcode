from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        sol = [str(num) for num in nums]
        sol.sort(key=lambda x: x*10, reverse=True)
        if sol[0] == "0":
            return "0"
        return ''.join(sol)