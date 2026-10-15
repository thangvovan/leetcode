from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sol = 0

        mini, maxi = min(nums), max(nums)
        count = [0] * (maxi - mini + 1)

        for num in nums:
            count[num - mini] += 1

        sum = 0
        for i in range(len(count)):
            if sum % 2 == 0:
                sol += (i + mini) * (count[i] // 2 + count[i] % 2)
            else:
                sol += (i + mini) * (count[i] // 2)
            sum += count[i]

        return sol