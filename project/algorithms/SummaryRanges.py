from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        sol = []

        s = nums[0]
        e = nums[0]
        for i in range(len(nums)):
            if i < len(nums)-1 and nums[i+1] - nums[i] == 1:
                e = nums[i+1]
            else:
                if s < e:
                    sol.append(f'{s}->{e}')
                else:
                    sol.append(str(s))


                if i != len(nums)-1:
                    s = nums[i+1]

        return sol